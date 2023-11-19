dataset_paths = {
	'anime_train_segmentation': '/kaggle/working/dds/Danbooru-Parsing/anime_seg_train',
	'anime_test_segmentation': '/kaggle/working/dds/Danbooru-Parsing/anime_seg_test_68',
	'anime_train': '/kaggle/working/dds/Danbooru-Parsing/anime_face_train',
	'anime_test': '/kaggle/working/dds/Danbooru-Parsing/anime_face_test_68',
    
	'face_train_segmentation': '/kaggle/working/dds/CelebaMask-HQ/celeba_seg_train',
	'face_test_segmentation': '/kaggle/working/dds/CelebaMask-HQ/celeba_seg_test_68',
	'face_train': '/kaggle/working/dds/CelebaMask-HQ/celeba_face_train',
	'face_test': '/kaggle/working/dds/CelebaMask-HQ/celeba_face_test_68',
}

model_paths = {
	'anime_ffhq': '/kaggle/working/pretrained_models/stylegan2_anime_pretrained.pt',
	'ir_se50': '/kaggle/working/pretrained_models/model_ir_se50.pth',
	'circular_face': '/kaggle/working/pretrained_models/CurricularFace_Backbone.pth',
	'mtcnn_pnet': '/kaggle/working/pretrained_models/mtcnn/pnet.npy',
	'mtcnn_rnet': '/kaggle/working/pretrained_models/mtcnn/rnet.npy',
	'mtcnn_onet': '/kaggle/working/pretrained_models/mtcnn/onet.npy',
	'shape_predictor': 'shape_predictor_68_face_landmarks.dat'
}
