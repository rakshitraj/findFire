import os
import cv2
from torchvision import datasets
import torchvision
import torch
import imutils
from torchvision.transforms import transforms
import torchvision.models as models
import numpy as np
from PIL import Image


def loadModel(path, cuda : bool):
    if cuda : 
        device = 'cuda'
    else: device = 'cpu'
    model = torch.load(path, map_location=torch.device(device))
    return model

def getPred(image, model):
    if not model:
        model = loadModel('/home/raxit/findFire/server/models/model_final.pth', False)
    class_names = ['Fire', 'Neutral', 'Smoke']
    # convert numpy array to PIL Image
    image = transforms.ToPILImage()(image)
    # Pipeline all transformations
    prediction_transform = transforms.Compose([transforms.Resize(size=(224, 224)), transforms.ToTensor(), transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])

    image
    image = prediction_transform(image)[:3,:,:].unsqueeze(0)
    #image = image.cuda()

    pred = model(image)
    idx = torch.argmax(pred)
    prob = pred[0][idx].item()*100
    
    return class_names[idx], prob

if __name__ == '__main__':
    model = loadModel(path='/home/raxit/findFire/server/models/model_final.pth', cuda=False)
    for path in ['res/test1.png','res/test2.png','res/test3.png'] :
        image = cv2.imread(path)
        print(getPred(image, model))
        cv2.imshow('Image', image)
        cv2.waitKey(0)