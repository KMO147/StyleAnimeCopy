path = '/kaggle/input/styleanimedata/'
dataset_paths = {
	'anime_train_segmentation': path + 'dds/Danbooru-Parsing/anime_seg_train',
	'anime_test_segmentation': path + 'dds/Danbooru-Parsing/anime_seg_test_68',
	'anime_train': path + 'dds/Danbooru-Parsing/anime_face_train',
	'anime_test': path + 'dds/Danbooru-Parsing/anime_face_test_68',
    
	'face_train_segmentation': path + 'dds/CelebaMask-HQ/celeba_seg_train',
	'face_test_segmentation': path + 'dds/CelebaMask-HQ/celeba_seg_test_68',
	'face_train': path + 'dds/CelebaMask-HQ/celeba_face_train',
	'face_test': path + 'dds/CelebaMask-HQ/celeba_face_test_68',
}

model_paths = {
	'anime_ffhq': path + 'pretrained_models/stylegan2_anime_pretrained.pt',
	'ir_se50': path + 'pretrained_models/model_ir_se50.pth',
	'circular_face': path + 'pretrained_models/CurricularFace_Backbone.pth',
	'mtcnn_pnet': path + 'pretrained_models/mtcnn/pnet.npy',
	'mtcnn_rnet': path + 'pretrained_models/mtcnn/rnet.npy',
	'mtcnn_onet': path + 'pretrained_models/mtcnn/onet.npy',
	'shape_predictor': 'shape_predictor_68_face_landmarks.dat'
}
