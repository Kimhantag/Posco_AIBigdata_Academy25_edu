#!/usr/bin/env python
# coding: utf-8

# In[4]:


# import pickle

# def load_boxes_info(filepath):
#     with open(filepath, 'rb') as f:
#         boxes_info = pickle.load(f)
#     return boxes_info

# # 파일 불러오기
# boxes_info = load_boxes_info('/home/piai/다운로드/Online-3D-BPP-pCT-density-code-add/data.pkl')
# # 처음 몇 개의 박스 정보만 출력
# for i, box in enumerate(boxes_info[:10]):  # 첫 10개만 출력
#     print(f"Box {i}: {box}")


# In[5]:


import pickle

def load_boxes_info(filepath):
    with open(filepath, 'rb') as f:
        boxes_info = pickle.load(f)
    return boxes_info

# 파일 불러오기
boxes_info = load_boxes_info('/home/piai/다운로드/Online-3D-BPP-pCT-density-code-add/logs/experiment/0415-3d-2024.04.15-00-32-58/PCT-0415-3d-2024.04.15-00-32-58_2024.04.15-00-32-59/data.pkl')
# 처음 몇 개의 박스 정보만 출력
for i, box in enumerate(boxes_info[:10]):  # 첫 10개만 출력
    print(f"Box {i}: {box}")


# In[6]:


# import pickle
# import torch

# class CustomUnpickler(pickle.Unpickler):
#     def persistent_load(self, pid):
#         # 'pid'는 저장된 객체의 고유 식별자입니다.
#         # 이 예제에서는 간단한 처리만을 수행하지만, 필요에 따라 복잡한 로직을 추가할 수 있습니다.
#         if pid[0] == 'torch.storage':
#             return torch.load(pid[1])
#         return None

# def load_boxes_info(filepath):
#     with open(filepath, 'rb') as f:
#         unpickler = CustomUnpickler(f)
#         boxes_info = unpickler.load()
#     return boxes_info

# # 파일 불러오기
# try:
#     boxes_info = load_boxes_info('/home/piai/다운로드/Online-3D-BPP-pCT-density-code-add/logs/experiment/0415-3d-2024.04.15-00-32-58/PCT-0415-3d-2024.04.15-00-32-58_2024.04.15-00-32-59/data.pkl')
#     for i, box in enumerate(boxes_info[:10]):  # 첫 10개만 출력
#         print(f"Box {i}: {box}")
# except Exception as e:
#     print(f"Error loading the data: {e}")


# In[7]:


# import pickle
# import torch

# class CustomUnpickler(pickle.Unpickler):
#     def persistent_load(self, pid):
#         type_tag, storage_type_str, *args = pid
#         if type_tag == 'torch.storage':
#             # 올바른 Storage 클래스를 찾고 인스턴스화합니다.
#             storage_class = getattr(torch, storage_type_str)  # 예: torch.FloatStorage
#             storage = storage_class(*args)  # args에는 필요한 추가 매개변수가 포함될 수 있습니다.
#             return storage
#         return None  # 적절한 처리가 가능하지 않은 경우 None을 반환

# def load_boxes_info(filepath):
#     with open(filepath, 'rb') as f:
#         unpickler = CustomUnpickler(f)
#         boxes_info = unpickler.load()
#     return boxes_info

# # 파일 불러오기 시도
# try:
#     boxes_info = load_boxes_info('/home/piai/다운로드/Online-3D-BPP-pCT-density-code-add/logs/experiment/0415-3d-2024.04.15-00-32-58/PCT-0415-3d-2024.04.15-00-32-58_2024.04.15-00-32-59/data.pkl')
#     for i, box in enumerate(boxes_info[:10]):
#         print(f"Box {i}: {box}")
# except Exception as e:
#     print(f"Error loading the data: {e}")


# In[2]:


# import pickle

# def load_boxes_info(filepath):
#     with open(filepath, 'rb') as f:
#         boxes_info = pickle.load(f)
#     return boxes_info

# # 파일 불러오기 예제
# try:
#     boxes_info = load_boxes_info('/home/piai/다운로드/Online-3D-BPP-pCT-density-code-add/logs/experiment/0414_3d-2024.04.14-23-53-26/PCT-0414_3d-2024.04.14-23-53-26_2024.04.14-23-53-34/data.pkl')
#     # 처음 몇 개의 박스 정보만 출력
#     for i, box in enumerate(boxes_info[:10]):  # 첫 10개만 출력
#         print(f"Box {i}: Size: {box['size']}, Position: {box['position']}, Bin Index: {box['bin_index']}")
# except Exception as e:
#     print(f"Error loading the data: {e}")


# In[3]:


# import pickle

# def persistent_load(persid):
#     # 여기서 `persid`를 처리하는 코드를 구현
#     # 예시: `persid`가 특정 타입을 참조할 때, 해당 타입의 객체를 생성하고 반환
#     print("Encountered persistent ID:", persid)
#     return None  # 또는 적절한 객체를 반환

# def load_boxes_info(filepath):
#     with open(filepath, 'rb') as f:
#         # `persistent_load`를 포함하여 pickle.load 호출
#         boxes_info = pickle.load(f, fix_imports=True, encoding="ASCII", errors="strict", persistent_load=persistent_load)
#     return boxes_info

# # 파일 불러오기 예제
# try:
#     boxes_info = load_boxes_info('/home/piai/다운로드/Online-3D-BPP-pCT-density-code-add/logs/experiment/0414_3d-2024.04.14-23-53-26/PCT-0414_3d-2024.04.14-23-53-26_2024.04.14-23-53-34/data.pkl')
#     for i, box in enumerate(boxes_info[:10]):
#         print(f"Box {i}: Size: {box['size']}, Position: {box['position']}, Bin Index: {box['bin_index']}")
# except Exception as e:
#     print(f"Error loading the data: {e}")


# In[4]:


# import pickle

# class CustomUnpickler(pickle.Unpickler):
#     def persistent_load(self, pid):
#         # 여기에서 pid를 처리하는 로직을 구현하세요.
#         # 예를 들어, 특정 타입의 객체를 반환하거나, 참조 ID에 따라 적절한 처리를 수행합니다.
#         print("Encountered persistent ID:", pid)
#         return None  # 실제 사용 시 적절한 객체로 대체 필요

# def load_boxes_info(filepath):
#     with open(filepath, 'rb') as f:
#         unpickler = CustomUnpickler(f)
#         boxes_info = unpickler.load()
#     return boxes_info

# # 파일 불러오기 예제
# try:
#     boxes_info = load_boxes_info('/home/piai/다운로드/Online-3D-BPP-pCT-density-code-add/logs/experiment/0414_3d-2024.04.14-23-53-26/PCT-0414_3d-2024.04.14-23-53-26_2024.04.14-23-53-34/data.pkl')
#     # 처음 몇 개의 박스 정보만 출력
#     for i, box in enumerate(boxes_info[:10]):  # 첫 10개만 출력
#         print(f"Box {i}: Size: {box['size']}, Position: {box['position']}, Bin Index: {box['bin_index']}")
# except Exception as e:
#     print(f"Error loading the data: {e}")


# In[5]:


# import torch
# print(torch.cuda.is_available())  # CUDA 사용 가능 여부 확인
# print(torch.cuda.current_device())  # 현재 CUDA 디바이스 인덱스 출력
# print(torch.cuda.get_device_name(0))  # 디바이스 이름 출력


# In[6]:


# class CustomUnpickler(pickle.Unpickler):
#     def persistent_load(self, pid):
#         # 'pid'는 ('storage', Storage_Type, '0', 'cuda:0', size) 형식의 튜플입니다.
#         type_tag, storage_type, location, device, size = pid
#         if type_tag == 'storage':
#             storage = storage_type(size)
#             storage = storage.cuda(device=device) if 'cuda' in device else storage
#             return storage
#         raise pickle.UnpicklingError("Unsupported persistent object found: {}".format(pid))
# def load_boxes_info(filepath):
#     with open(filepath, 'rb') as f:
#         unpickler = CustomUnpickler(f)
#         boxes_info = unpickler.load()
#     return boxes_info

# # 파일 불러오기
# try:
#     boxes_info = load_boxes_info('/home/piai/다운로드/Online-3D-BPP-pCT-density-code-add/logs/experiment/0414_3d-2024.04.14-23-53-26/PCT-0414_3d-2024.04.14-23-53-26_2024.04.14-23-53-34/data.pkl')
#     for i, box in enumerate(boxes_info[:10]):
#         print(f"Box {i}: Size: {box['size']}, Position: {box['position']}, Bin Index: {box['bin_index']}")
# except Exception as e:
#     print(f"Error loading the data: {e}")


# In[7]:


# import pickle
# import torch

# class CustomUnpickler(pickle.Unpickler):
#     def persistent_load(self, pid):
#         # pid 형식: ('storage', <class 'torch.FloatStorage'>, '0', 'cuda:0', size)
#         type_tag, storage_type, obj_key, device, size = pid
#         if type_tag == 'storage':
#             # 적절한 디바이스에 저장소 객체를 생성합니다.
#             storage = storage_type(size)
#             if 'cuda' in device:
#                 # 디바이스 설정으로 CUDA GPU를 지정합니다.
#                 device_id = int(device.split(':')[-1])  # 'cuda:0' -> 0
#                 storage = storage.cuda(device=device_id)
#             return storage
#         else:
#             raise pickle.UnpicklingError(f"Unsupported persistent object found: {pid}")

# def load_boxes_info(filepath):
#     with open(filepath, 'rb') as f:
#         unpickler = CustomUnpickler(f)
#         boxes_info = unpickler.load()
#     return boxes_info

# # 파일 불러오기 예제
# try:
#     boxes_info = load_boxes_info('/home/piai/다운로드/Online-3D-BPP-pCT-density-code-add/logs/experiment/0414_3d-2024.04.14-23-53-26/PCT-0414_3d-2024.04.14-23-53-26_2024.04.14-23-53-34/data.pkl')
#     # 처음 몇 개의 박스 정보만 출력
#     for i, box in enumerate(boxes_info[:10]):  # 첫 10개만 출력
#         print(f"Box {i}: Size: {box['size']}, Position: {box['position']}, Bin Index: {box['bin_index']}")
# except Exception as e:
#     print(f"Error loading the data: {e}")


# In[8]:


# import pickle
# import torch

# class CustomUnpickler(pickle.Unpickler):
#     def persistent_load(self, pid):
#         type_tag, storage_type, location, device, size = pid
#         if type_tag == 'storage':
#             try:
#                 # 정확한 데이터 타입과 사이즈로 storage 객체를 생성합니다.
#                 if isinstance(size, int):
#                     storage = storage_type(size)
#                 else:
#                     raise ValueError("Invalid size for storage creation.")

#                 # 적절한 디바이스 설정
#                 if 'cuda' in device:
#                     device_id = int(device.split(':')[-1])
#                     storage = storage.cuda(device=device_id)
#                 return storage
#             except Exception as e:
#                 raise pickle.UnpicklingError(f"Error creating storage: {e}")

#         raise pickle.UnpicklingError("Unsupported persistent object found: {}".format(pid))


# def load_boxes_info(filepath):
#     with open(filepath, 'rb') as f:
#         unpickler = CustomUnpickler(f)
#         boxes_info = unpickler.load()
#     return boxes_info

# # 파일 불러오기 예제
# try:
#     boxes_info = load_boxes_info('/home/piai/다운로드/Online-3D-BPP-pCT-density-code-add/logs/experiment/0414_3d-2024.04.14-23-53-26/PCT-0414_3d-2024.04.14-23-53-26_2024.04.14-23-53-34/data.pkl')
#     # 처음 몇 개의 박스 정보만 출력
#     for i, box in enumerate(boxes_info[:10]):  # 첫 10개만 출력
#         print(f"Box {i}: Size: {box['size']}, Position: {box['position']}, Bin Index: {box['bin_index']}")
# except Exception as e:
#     print(f"Error loading the data: {e}")


# In[1]:


# import pickle
# import torch

# class CustomUnpickler(pickle.Unpickler):
#     def persistent_load(self, pid):
#         type_tag, storage_type, location, device, size = pid
#         if type_tag == 'storage':
#             try:
#                 # 정확한 데이터 타입과 사이즈로 storage 객체를 생성합니다.
#                 if isinstance(size, int):
#                     storage = storage_type(size)
#                 else:
#                     raise ValueError("Invalid size for storage creation.")

#                 # 적절한 디바이스 설정
#                 if 'cuda' in device:
#                     device_id = int(device.split(':')[-1])
#                     storage = storage.cuda(device=device_id)
#                 return storage
#             except Exception as e:
#                 raise pickle.UnpicklingError(f"Error creating storage: {e}")

#         raise pickle.UnpicklingError("Unsupported persistent object found: {}".format(pid))


# def load_boxes_info(filepath):
#     with open(filepath, 'rb') as f:
#         unpickler = CustomUnpickler(f)
#         boxes_info = unpickler.load()
#     return boxes_info

# # 파일 불러오기 예제
# try:
#     boxes_info = load_boxes_info('/home/piai/다운로드/Online-3D-BPP-pCT-density-code-add/logs/experiment/0415-3d-2024.04.15-00-32-58/PCT-0415-3d-2024.04.15-00-32-58_2024.04.15-00-32-59/data.pkl')
#     # 데이터 사용 예시
#     some_dict = {}
#     for i, box in enumerate(boxes_info[:10]):
#         # 데이터를 튜플로 변환하여 딕셔너리의 키로 사용
#         key = (box['size'], tuple(box['position']))  # 변경 가능한 타입을 튜플로 변환
#         some_dict[key] = box['bin_index']
#         print(f"Box {i}: Size: {box['size']}, Position: {box['position']}, Bin Index: {box['bin_index']}")
# except Exception as e:
#     print(f"Error loading the data: {e}")


# In[3]:


# import pickle
# import torch

# class CustomUnpickler(pickle.Unpickler):
#     def persistent_load(self, pid):
#         type_tag, storage_type, location, device, size = pid
#         if type_tag == 'storage':
#             try:
#                 storage = storage_type(size)
#                 if 'cuda' in device:
#                     device_id = int(device.split(':')[-1])
#                     storage = storage.cuda(device=device_id)
#                 return storage
#             except Exception as e:
#                 raise pickle.UnpicklingError(f"Error creating storage: {e}")
#         raise pickle.UnpicklingError("Unsupported persistent object found: {}".format(pid))

# def load_boxes_info(filepath):
#     with open(filepath, 'rb') as f:
#         unpickler = CustomUnpickler(f)
#         boxes_info = unpickler.load()
#     return boxes_info

# # 파일 불러오기 예제
# try:
#     boxes_info = load_boxes_info('/home/piai/다운로드/Online-3D-BPP-pCT-density-code-add/logs/experiment/0415-3d-2024.04.15-00-32-58/PCT-0415-3d-2024.04.15-00-32-58_2024.04.15-00-32-59/data.pkl')
#     some_dict = {}
#     for i, box in enumerate(boxes_info[:10]):
#         print(f"Checking box {i} position type: {type(box['position'])}")
#         if isinstance(box['position'], (list, tuple)):  # Ensure it's list or tuple
#             position_tuple = tuple(box['position'])
#             key = (box['size'], position_tuple)
#             some_dict[key] = box['bin_index']
#             print(f"Box {i}: Size: {box['size']}, Position: {position_tuple}, Bin Index: {box['bin_index']}")
#         else:
#             print(f"Invalid type for position: {type(box['position'])}")
# except Exception as e:
#     print(f"Error loading the data: {e}")


# In[10]:


# # 파일 불러오기 예제
# try:
#     boxes_info = load_boxes_info('/home/piai/다운로드/Online-3D-BPP-pCT-density-code-add/logs/experiment/0414_3d-2024.04.14-23-53-26/PCT-0414_3d-2024.04.14-23-53-26_2024.04.14-23-53-34/data.pkl')
#     for i, box in enumerate(boxes_info[:10]):
#         print(f"Box {i}: {box}")
# except Exception as e:
#     print(f"Error loading the data: {e}")


# In[11]:


# # 파일 불러오기 예제
# try:
#     boxes_info = load_boxes_info('/home/piai/다운로드/Online-3D-BPP-pCT-density-code-add/logs/experiment/0414_3d-2024.04.14-23-53-26/PCT-0414_3d-2024.04.14-23-53-26_2024.04.14-23-53-34/data.pkl')
#     for i, box in enumerate(boxes_info[:10]):
#         print(f"Box {i}: Position type: {type(box['position'])}")
# except Exception as e:
#     print(f"Error loading the data: {e}")


# In[12]:


# # 파일 불러오기 예제
# try:
#     boxes_info = load_boxes_info('/home/piai/다운로드/Online-3D-BPP-pCT-density-code-add/logs/experiment/0414_3d-2024.04.14-23-53-26/PCT-0414_3d-2024.04.14-23-53-26_2024.04.14-23-53-34/data.pkl')
#     some_dict = {}
#     for i, box in enumerate(boxes_info):
#         if isinstance(box['position'], list):
#             key = (box['size'], tuple(box['position']))
#         else:
#             key = (box['size'], box['position'])
#         some_dict[key] = box['bin_index']
#         print(f"Box {i}: Size: {box['size']}, Position: {box['position']}, Bin Index: {box['bin_index']}")
# except Exception as e:
#     print(f"Error loading the data: {e}")


# In[13]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# # 3D 그래프 초기화
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # 박스 정보를 이용하여 3D 상자 그리기
# for box in boxes_info[0]:  # 첫 번째 박스 정보만 사용
#     x, y, z, _ = box  # 마지막 값은 밀도 또는 다른 메트릭으로 추정되므로, 여기서는 사용하지 않음
#     # x, y, z 위치에서 시작하고, 각 크기 만큼 상자 그리기
#     ax.bar3d(x, y, z, 1, 1, 1, alpha=0.8)  # dx, dy, dz 크기를 1로 설정하여 큐브 형태로 표현

# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.title('3D Box Plot')
# plt.show()

# 3D 그래프 초기화
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 박스 정보를 이용하여 3D 상자 그리기
for box in boxes_info[0]:  # 첫 번째 박스 정보만 사용
    x, y, z = box  # 밀도 또는 다른 메트릭은 사용하지 않음
    # x, y, z 위치에서 시작하고, 각 크기 만큼 상자 그리기
    ax.bar3d(x, y, z, 1, 1, 1, alpha=0.8)  # dx, dy, dz 크기를 1로 설정하여 큐브 형태로 표현

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('3D Box Plot')
plt.show()


# In[ ]:




