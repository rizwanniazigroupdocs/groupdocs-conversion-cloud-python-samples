# Import modules
import groupdocs_conversion_cloud
from Common_Utilities.Utils import Common_Utilities


class Conversion_Python_Convert_To_Cells:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_ConvertApi_Instance()
        
        try:
            settings = groupdocs_conversion_cloud.ConvertSettings()
            settings.storage_name = Common_Utilities.myStorage;
            settings.file_path = "conversions\\password-protected.docx"
            settings.format = "xlsx"
            
            loadOptions = groupdocs_conversion_cloud.DocxLoadOptions()
            loadOptions.password = "password"
            
            settings.load_options = loadOptions;
            
            convertOptions = groupdocs_conversion_cloud.XlsxConvertOptions()
            convertOptions.from_page = 1
            convertOptions.pages_count = 1
            convertOptions.password = "password"
            convertOptions.use_pdf = False
            
            settings.convert_options = convertOptions
            settings.output_path = "converted\\tocells"
            
            request = groupdocs_conversion_cloud.ConvertDocumentRequest(settings)
            response = api.convert_document(request)

            print("Document converted successfully: " + str(response))
        except groupdocs_conversion_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))