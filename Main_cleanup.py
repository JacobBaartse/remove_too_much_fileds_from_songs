import presentation_pb2
from pathlib import Path
import os


def remove_too_much_fields(filename_input, output_dir, filename_output, fields_to_keep):
    print(filename_output)
    presentation_obj = presentation_pb2.Presentation()
    with open(filename_input, mode='rb') as pro_file:
        presentation_obj.ParseFromString(pro_file.read())

    for que_idx in range(len(presentation_obj.cues)):
        for action_idx in range(len(presentation_obj.cues[que_idx].actions)):
            del_count = 0
            for element_idx in range(len(presentation_obj.cues[que_idx].actions[action_idx].slide.presentation.base_slide.elements)):
                # print(presentation_obj.cues[que_idx].actions[action_idx].slide.presentation.base_slide.elements[element_idx])
                field_name = presentation_obj.cues[que_idx].actions[action_idx].slide.presentation.base_slide.elements[element_idx-del_count].element.name
                # print("field name: ", field_name)
                if field_name in fields_to_keep:
                    pass
                else:
                    del presentation_obj.cues[que_idx].actions[action_idx].slide.presentation.base_slide.elements[element_idx-del_count]
                    del_count += 1

    if os.path.exists(output_dir):
        pass
    else:
        os.makedirs(output_dir)
    with open(filename_output, "wb") as pro_file:
        pro_file.write(presentation_obj.SerializeToString())


if __name__ == "__main__":

    # adapt the following settings to your needs
    # =============================================
    fields_to_keep = ("Engels", "Vertaling", "Aanwijzing")
    directory_in = r"C:\songs"
    directory_out = r"C:\songs_new"
    # =============================================

    path_list = Path(directory_in).rglob('*.pro')
    for path in path_list:
        output_dir = str(path.parent).replace(directory_in, directory_out)
        output_file = str(path).replace(directory_in, directory_out)
        remove_too_much_fields(path,
                               output_dir,
                               output_file,
                               fields_to_keep)
