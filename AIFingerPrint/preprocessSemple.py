import cv2
import matplotlib.pyplot as plt
import numpy as np

import glob, os


def extract_label(img_path):
    filename, _ = os.path.splitext(os.path.basename(img_path))
    
    subject_id, etc = filename.split('__')
    gender, lr, finger, _ = etc.split('_')
    
    gender = 0 if gender == 'M' else 1
    lr = 0 if lr =='Left' else 1
    
    if finger == 'thumb':
        finger = 0
    elif finger == 'index':
        finger = 1
    elif finger == 'middle':
        finger = 2
    elif finger == 'ring':
        finger = 3
    elif finger == 'little':
        finger = 4
        
    return np.array([subject_id, gender, lr, finger], dtype=np.uint16)

def extract_label2(img_path):
    filename, _ = os.path.splitext(os.path.basename(img_path))
    
    subject_id, etc = filename.split('__')
    gender, lr, finger, _, _ = etc.split('_')
    
    gender = 0 if gender == 'M' else 1
    lr = 0 if lr =='Left' else 1
    
    if finger == 'thumb':
        finger = 0
    elif finger == 'index':
        finger = 1
    elif finger == 'middle':
        finger = 2
    elif finger == 'ring':
        finger = 3
    elif finger == 'little':
        finger = 4
        
    return np.array([subject_id, gender, lr, finger], dtype=np.uint16)


# In[37]:


img_list = sorted(glob.glob('*.bmp'))
print(len(img_list))

imgs = np.empty((len(img_list), 96, 96), dtype=np.uint8)
labels = np.empty((len(img_list), 4), dtype=np.uint16)

for i, img_path in enumerate(img_list):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (96, 96))
    imgs[i] = img
    
    # subject_id, gender, lr, finger
    labels[i] = extract_label(img_path)
    
np.save('dataset/x_real.npy', imgs)
np.save('dataset/y_real.npy', labels)

plt.figure(figsize=(1, 1))
plt.title(labels[-1])
plt.imshow(imgs[-1], cmap='gray')

plt.show()
# In[40]:


img_list = sorted(glob.glob('Altered/Altered-Easy/*.BMP'))
print(len(img_list))

imgs = np.empty((len(img_list), 96, 96), dtype=np.uint8)
labels = np.empty((len(img_list), 4), dtype=np.uint16)

for i, img_path in enumerate(img_list):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (96, 96))
    imgs[i] = img
    
    # subject_id, gender, lr, finger
    labels[i] = extract_label2(img_path)
    
np.save('dataset/x_easy.npy', imgs)
np.save('dataset/y_easy.npy', labels)

plt.figure(figsize=(1, 1))
plt.title(labels[-1])
plt.imshow(imgs[-1], cmap='gray')

plt.show()
# In[42]:


img_list = sorted(glob.glob('Altered/Altered-Medium/*.BMP'))
print(len(img_list))

imgs = np.empty((len(img_list), 96, 96), dtype=np.uint8)
labels = np.empty((len(img_list), 4), dtype=np.uint16)

for i, img_path in enumerate(img_list):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (96, 96))
    imgs[i] = img
    
    # subject_id, gender, lr, finger
    labels[i] = extract_label2(img_path)
    
np.save('dataset/x_medium.npy', imgs)
np.save('dataset/y_medium.npy', labels)

plt.figure(figsize=(1, 1))
plt.title(labels[-1])
plt.imshow(imgs[-1], cmap='gray')

plt.show()
# In[43]:


img_list = sorted(glob.glob('Altered/Altered-Hard/*.BMP'))
print(len(img_list))

imgs = np.empty((len(img_list), 96, 96), dtype=np.uint8)
labels = np.empty((len(img_list), 4), dtype=np.uint16)

for i, img_path in enumerate(img_list):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (96, 96))
    imgs[i] = img
    
    # subject_id, gender, lr, finger
    labels[i] = extract_label2(img_path)
    
np.save('dataset/x_hard.npy', imgs)
np.save('dataset/y_hard.npy', labels)

plt.figure(figsize=(1, 1))
plt.title(labels[-1])
plt.imshow(imgs[-1], cmap='gray')

plt.show()
# In[ ]:




