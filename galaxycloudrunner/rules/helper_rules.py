import os

from galaxy.util import size_to_bytes


def __get_dataset_size(dataset_association):
    try:
        return os.path.getsize(dataset_association.dataset.file_name)
    except os.error:
        return 0


def __sum_total(prev, current):
    return prev + current


def __calculate_dataset_total(datasets):
    if datasets:
        return reduce(__sum_total,
                      map(__get_dataset_size, datasets))
    else:
        return 0


def to_destination_if_size(job, max_size, to_destination_id,
                           fallback_destination_id):
    """
    A rule that will route a job to the "to_destination_id" if
    the input size is below a certain threshold, or to the
    "fallback_destination_id" if not.
    """
    total_input_size = __calculate_dataset_total(job.input_datasets)
    total_library_size = __calculate_dataset_total(job.input_library_datasets)
    if (total_input_size+total_library_size) <= size_to_bytes(max_size):
        return to_destination_id
    else:
        return fallback_destination_id
