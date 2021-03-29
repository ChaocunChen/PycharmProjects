import os
import sys
import argparse
import cv2
import numpy as np
from PIL import Image, ImageDraw
from google.protobuf import text_format

def get_labelname(labelmap, labels):
    num_labels = len(labelmap.item)
    labelnames = []
    if type(labels) is not list:
        labels = [labels]
    for label in labels:
        found = False
        for i in xrange(0, num_labels):
            if label == labelmap.item[i].label:
                found = True
                labelnames.append(labelmap.item[i].display_name)
                break
        assert found == True
    return labelnames
sleep_time=0
class CaffeDetection:
    def __init__(self, model_def, model_weights, image_resize, labelmap_file, caffe_root):
        # caffe.set_device(gpu_id)
        # caffe_root = '/home/ubuntu/caffe_ssd'
        os.chdir(caffe_root)  # 切换到caffe_root目录
        sys.path.insert(0, os.path.join(caffe_root, 'python'))
        import caffe
        from caffe.proto import caffe_pb2
        caffe.set_mode_gpu()

        self.image_resize = image_resize
        # Load the net in the test phase for inference, and configure input preprocessing.
        self.net = caffe.Net(model_def,  # defines the structure of the model
                             model_weights,  # contains the trained weights
                             caffe.TEST)  # use test mode (e.g., don't perform dropout)
        # input preprocessing: 'data' is the name of the input blob == net.inputs[0]
        self.transformer = caffe.io.Transformer({'data': self.net.blobs['data'].data.shape})
        self.transformer.set_transpose('data', (2, 0, 1))
        self.transformer.set_mean('data', np.array([104, 117, 123]))  # mean pixel
        # the reference model operates on images in [0,255] range instead of [0,1]
        self.transformer.set_raw_scale('data', 255)
        # the reference model has channels in BGR order instead of RGB
        self.transformer.set_channel_swap('data', (2, 1, 0))

        # load PASCAL VOC labels
        file = open(labelmap_file, 'r')
        self.labelmap = caffe_pb2.LabelMap()
        text_format.Merge(str(file.read()), self.labelmap)

        def detect(self, image_file, conf_thresh=0.8, topn=100):
            '''
            SSD detection
            '''
            import caffe
            self.net.blobs['data'].reshape(1, 3, self.image_resize, self.image_resize)
            # image = caffe.io.load_image(image_file)
            image = image_file  #
            image = image[..., ::-1]  # 3个#操作代替caffe.io.load_image(image_file)
            image = image / 255.0  #
            # print(image)

            # Run the net and examine the top_k results
            transformed_image = self.transformer.preprocess('data', image)
            self.net.blobs['data'].data[...] = transformed_image

            # Forward pass.
            detections = self.net.forward()['detection_out']

            # Parse the outputs.
            det_label = detections[0, 0, :, 1]
            det_conf = detections[0, 0, :, 2]
            det_xmin = detections[0, 0, :, 3]
            det_ymin = detections[0, 0, :, 4]
            det_xmax = detections[0, 0, :, 5]
            det_ymax = detections[0, 0, :, 6]

            # Get detections with confidence higher than 0.6.
            top_indices = [i for i, conf in enumerate(det_conf) if conf >= conf_thresh]

            top_conf = det_conf[top_indices]
            top_label_indices = det_label[top_indices].tolist()
            top_labels = get_labelname(self.labelmap, top_label_indices)
            top_xmin = det_xmin[top_indices]
            top_ymin = det_ymin[top_indices]
            top_xmax = det_xmax[top_indices]
            top_ymax = det_ymax[top_indices]

            result = []
            for i in xrange(min(topn, top_conf.shape[0])):
                xmin = int(round(top_xmin[i] * image.shape[1]))
                # print(image.shape[1])
                ymin = int(round(top_ymin[i] * image.shape[0]))
                xmax = int(round(top_xmax[i] * image.shape[1]))
                ymax = int(round(top_ymax[i] * image.shape[0]))
                score = top_conf[i]
                label = int(top_label_indices[i])
                label_name = top_labels[i]
                result.append([xmin, ymin, xmax, ymax, label, score, label_name])
            return result

def test_video(args):
    detection = CaffeDetection(args.model_def, args.model_weights,
                               args.image_resize, args.labelmap_file, args.caffe_root)

    cap = cv2.VideoCapture('/home/chenchaocun/caffe-ssd/Can/IMG_1318.mp4')
    #cap = cv2.VideoCapture('/home/chenchaocun/caffe-ssd/Can/IMG_1253.MOV')

    while(cap.isOpened()):
        ret, frame = cap.read()
        #print(frame.shape)
        result = detection.detect(frame, args.thresh)

        for item in result:
            cv2.rectangle(frame, (item[0], item[1]), (item[2], item[3]), (0,255,0), 2)
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(frame, str(item[6])+' '+str(item[5]), (item[0]+20,item[1]+20), font, 1, (0,0,255), 1)
            if str(item[6])=='sleep':
                sleep_time+=1

                if sleep_time >=5:
                    print('sleeping!')

        cv2.imshow('image', frame)
        k = cv2.waitKey(1)
        if (k & 0xff == ord('q')):
            break

def parse_args():
    '''parse args'''
    parser = argparse.ArgumentParser()
    # parser.add_argument('--gpu_id', type=int, default=0, help='gpu id')
    parser.add_argument('--labelmap_file',
                        default='/home/chenchaocun/caffe-ssd/Can/labelmap_voc.prototxt')
    parser.add_argument('--model_def',
                        default='/home/chenchaocun/caffe-ssd/Can/deploy-Can-384-8.prototxt')
    parser.add_argument('--image_resize', default=384, type=int)
    parser.add_argument('--thresh', default=0.3, type=float)
    parser.add_argument('--model_weights',
                        default='/home/chenchaocun/caffe-ssd/Can/Can-384_iter_20000.caffemodel')
    parser.add_argument('--caffe_root', default='/home/chenchaocun/caffe_ssd_CenterLoss')
    return parser.parse_args()
if __name__ == '__main__':
    test_video(parse_args())

