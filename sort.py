import os
import shutil
import random
from pathlib import Path

def split_dataset(root_dir, output_dir, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15):
    assert train_ratio + val_ratio + test_ratio == 1.0

    random.seed(42)

    classes = [d.name for d in Path(root_dir).iterdir() if d.is_dir()]
    
    for cls in classes:
        cls_path = Path(root_dir) / cls
        images = list(cls_path.glob('*'))  # optional: filter by suffix
        
        random.shuffle(images)
        total = len(images)
        train_end = int(train_ratio * total)
        val_end = train_end + int(val_ratio * total)

        splits = {
            'train': images[:train_end],
            'val': images[train_end:val_end],
            'test': images[val_end:]
        }

        for split, imgs in splits.items():
            split_dir = Path(output_dir) / split / cls
            split_dir.mkdir(parents=True, exist_ok=True)
            for img in imgs:
                shutil.copy(img, split_dir / img.name)

split_dataset("RealWaste", "RealWaste_split")
