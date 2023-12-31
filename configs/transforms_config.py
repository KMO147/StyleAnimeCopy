from abc import abstractmethod
import torchvision.transforms as transforms
from dataset import augmentations


class TransformsConfig(object):

	def __init__(self, opts):
		self.opts = opts

	@abstractmethod
	def get_transforms(self):
		pass


class SegToImageTransforms(TransformsConfig):

	def __init__(self, opts):
		super(SegToImageTransforms, self).__init__(opts)

	def get_transforms(self):
		transforms_dict = {
			'transform_gt_train': transforms.Compose([
				transforms.Resize((256, 256)),
				transforms.ToTensor(),
				transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])]),
			'transform_source': transforms.Compose([
				transforms.Resize((256, 256)),
				augmentations.ToOneHot(self.opts.label_nc),
				transforms.ToTensor()]),
			'transform_test': transforms.Compose([
				transforms.Resize((256, 256)),
				transforms.ToTensor(),
				transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])]),
			'transform_inference': transforms.Compose([
				transforms.Resize((256, 256)),
				augmentations.ToOneHot(self.opts.label_nc),
				transforms.ToTensor()])
		}
		return transforms_dict

