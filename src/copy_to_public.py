import os
import shutil

def copy_conetent(source_dir, dest_dir):
    if not os.path.exists(source_dir) or not os.path.exists(dest_dir):
        raise Exception("Source directory or destination directory doesn't exist")
    in_dest_dir = os.listdir(dest_dir)
    if source_dir == "./static":
        for item in in_dest_dir:
            path_to_item = os.path.join(dest_dir, item)
            print(f"Removing {item} from {dest_dir}")
            if os.path.isdir(path_to_item):
                shutil.rmtree(path_to_item)
            else:
                os.remove(path_to_item)
    in_src_dir = os.listdir(source_dir)
    for item in in_src_dir:
        path_to_item = os.path.join(source_dir, item)
        if os.path.isfile(path_to_item):
            shutil.copy(path_to_item, dest_dir)
            print(f"Added {path_to_item} to {dest_dir}")
        elif os.path.isdir(path_to_item):
            # copy this dest_dir/dir
            dir_to_copy = path_to_item.split("/")[-1]
            copy_dir_path = os.path.join(dest_dir, dir_to_copy)
            os.mkdir(copy_dir_path)
            print(f"Thid is the new dir {copy_dir_path}")
            copy_conetent(path_to_item, copy_dir_path)
        else:
            continue
