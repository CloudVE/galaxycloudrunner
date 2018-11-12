import os

from galaxy.util import size_to_bytes


def __get_dataset_size(dataset_association):
    try:
        return os.path.getsize(dataset_association.dataset.file_name)
    except os.error:
        return 0


def __sum_total(prev, current):
    return prev + current


def to_destination_if_size(job, max_size, to_destination_id,
                           fallback_destination_id):
    """
    A rule that will route a job to the "to_destination_id" if
    the input size is below a certain threshold, or to the
    "fallback_destination_id" if not.
    """
    total_input_size = (reduce(
        __sum_total, map(__get_dataset_size, job.input_datasets))
        if job.input_datasets else 0)
    total_library_size = (reduce(
        __sum_total, map(__get_dataset_size, job.input_library_datasets))
        if job.input_library_datasets else 0)
    if (total_input_size+total_library_size) <= size_to_bytes(max_size):
        return to_destination_id
    else:
        return fallback_destination_id
