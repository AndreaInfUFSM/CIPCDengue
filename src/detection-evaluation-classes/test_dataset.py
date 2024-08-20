from tf_dataset import TFDataset
from yolo_dataset import YoloDataset
from boundingbox_visualizer import BoundingBoxVisualizer




def test_visualize_single_image(fname, dataset_class, dataset_path):

    dataset = dataset_class(dataset_path)
    unique_classes = dataset.get_unique_classes()
    image, bboxes, labels = dataset.get_entry_by_fname(fname)

    visualizer = BoundingBoxVisualizer(unique_classes)
    visualizer.show_bboxes(image, bboxes, labels)


def test_inspect_dataset(dataset_name, dataset_class, dataset_path):

    dataset = dataset_class(dataset_path)

    print(f"\n==>{dataset_name} Dataset statistics:")
    stats = dataset.get_stats()
    print("\n".join(f"{key}: {value}" for key, value in stats.items())) 

    print('\n==> Unique classes for this dataset')
    unique_classes = dataset.get_unique_classes()
    print(unique_classes)

    print('\n==> Objects per image')
    truth_bboxes, truth_labels = dataset.get_groundtruth_per_image()
    for key, value in truth_bboxes.items():
        print(key, len(value))


def main():

    tf_test_dataset_path = '/home/andrea/Dropbox/lsc/dengue/training-round-02/round-02-tiled-training-dataset/v5-test.tfrecord'
    test_inspect_dataset('Tensorflow', TFDataset, tf_test_dataset_path)
    test_visualize_single_image('0', TFDataset, tf_test_dataset_path)


    yolo_test_dataset_path = '/home/andrea/Dropbox/lsc/dengue/training-round-02/root-dir-to-upload/images/test/'
    test_inspect_dataset('Yolo', YoloDataset, yolo_test_dataset_path)
    test_visualize_single_image('000000000379.jpg', YoloDataset, yolo_test_dataset_path)



if __name__ == "__main__":
    main()