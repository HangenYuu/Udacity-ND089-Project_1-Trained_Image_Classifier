from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
in_arg = get_input_args()
results = get_pet_labels(in_arg.dir)
classify_images(in_arg.dir, results, in_arg.arch)
print(results)