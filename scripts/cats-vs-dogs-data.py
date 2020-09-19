import os
import shutil

original_dir = "/Users/camargo/Projects/deeplearning/data/dogs-vs-cats/train"

new_dir = "/Users/camargo/Projects/deeplearning/data/dogs-vs-cats-small"
os.mkdir(new_dir)

train_dir = os.path.join(new_dir, "train")
os.mkdir(train_dir)
validation_dir = os.path.join(new_dir, "validation")
os.mkdir(validation_dir)
test_dir = os.path.join(new_dir, "test")
os.mkdir(test_dir)

train_cats_dir = os.path.join(train_dir, "cats")
os.mkdir(train_cats_dir)
train_dogs_dir = os.path.join(train_dir, "dogs")
os.mkdir(train_dogs_dir)

validation_cats_dir = os.path.join(validation_dir, "cats")
os.mkdir(validation_cats_dir)
validation_dogs_dir = os.path.join(validation_dir, "dogs")
os.mkdir(validation_dogs_dir)

test_cats_dir = os.path.join(test_dir, "cats")
os.mkdir(test_cats_dir)
test_dogs_dir = os.path.join(test_dir, "dogs")
os.mkdir(test_dogs_dir)

file_names = [f"cat.{i}.jpg" for i in range(1000)]
for file_name in file_names:
    src = os.path.join(original_dir, file_name)
    dst = os.path.join(train_cats_dir, file_name)
    shutil.copyfile(src, dst)

file_names = [f"cat.{i}.jpg" for i in range(1000, 1500)]
for file_name in file_names:
    src = os.path.join(original_dir, file_name)
    dst = os.path.join(validation_cats_dir, file_name)
    shutil.copyfile(src, dst)

file_names = [f"cat.{i}.jpg" for i in range(1500, 2000)]
for file_name in file_names:
    src = os.path.join(original_dir, file_name)
    dst = os.path.join(test_cats_dir, file_name)
    shutil.copyfile(src, dst)

file_names = [f"dog.{i}.jpg" for i in range(1000)]
for file_name in file_names:
    src = os.path.join(original_dir, file_name)
    dst = os.path.join(train_dogs_dir, file_name)
    shutil.copyfile(src, dst)

file_names = [f"dog.{i}.jpg" for i in range(1000, 1500)]
for file_name in file_names:
    src = os.path.join(original_dir, file_name)
    dst = os.path.join(validation_dogs_dir, file_name)
    shutil.copyfile(src, dst)

file_names = [f"dog.{i}.jpg" for i in range(1500, 2000)]
for file_name in file_names:
    src = os.path.join(original_dir, file_name)
    dst = os.path.join(test_dogs_dir, file_name)
    shutil.copyfile(src, dst)

print(f"total training cat images: {len(os.listdir(train_cats_dir))}")
print(f"total training dog images: {len(os.listdir(train_dogs_dir))}")
print(f"total validation cat images: {len(os.listdir(validation_cats_dir))}")
print(f"total validation dog images: {len(os.listdir(validation_dogs_dir))}")
print(f"total test cat images: {len(os.listdir(test_cats_dir))}")
print(f"total test dog images {len(os.listdir(test_dogs_dir))}")
