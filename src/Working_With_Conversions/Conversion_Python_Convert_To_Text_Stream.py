# Import modules
import groupdocs_conversion_cloud
from Common_Utilities.Utils import Common_Utilities


class Conversion_Python_Convert_To_Text_Stream:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_ConvertApi_Instance()
        
        try:
            settings = groupdocs_conversion_cloud.ConvertSettings()
            settings.storage_name = Common_Utilities.myStorage;
            settings.file_path = "conversions\\sample.docx"
            settings.format = "txt"
            
            loadOptions = groupdocs_conversion_cloud.DocxLoadOptions()
            loadOptions.hide_word_tracked_changes = True
            loadOptions.default_font = "Arial"
            
            settings.load_options = loadOptions;
            
            convertOptions = groupdocs_conversion_cloud.TxtConvertOptions()
            convertOptions.from_page = 1
            convertOptions.pages_count = 1
    
            settings.convert_options = convertOptions
            settings.output_path = None  # leave OutputPath will result the output as document IOStream
            
            request = groupdocs_conversion_cloud.ConvertDocumentRequest(settings)
            response = api.convert_document_download(request)

            print("Document converted successfully: " + str(len(response)))
        except groupdocs_conversion_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))
