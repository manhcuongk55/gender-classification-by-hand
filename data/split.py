import shutil

with open('test.csv', 'r') as f:
    lines = f.readlines()
    for line in lines:
        image, gender = line.split(",")
        print(image)
        if 'female' in gender:
            shutil.move("test/" + image, "test/female/" + image)
        else:
            shutil.move("test/" + image, "test/male/" + image)
