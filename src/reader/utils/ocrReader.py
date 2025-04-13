import easyocr
import os

class OCRReader:
    _instance = None
    
    @classmethod
    def get_instance(cls, languages=None, gpu=True, model_storage_directory=None):
        """
        Get or create a singleton instance of the OCR reader.
        
        Args:
            languages (list): List of languages to use (default: ['en'])
            gpu (bool): Whether to use GPU (default: True)
            model_storage_directory (str): Directory to store models
            
        Returns:
            The OCR reader instance
        """
        if cls._instance is None:
            if languages is None:
                languages = ['en']
                
            cls._instance = easyocr.Reader(
                languages,
                gpu=gpu,
                model_storage_directory=model_storage_directory
            )
        return cls._instance
    
    @staticmethod
    def read_text(image, detail=1, paragraph=False, **kwargs):
        """
        Read text from an image using the OCR reader.
        
        Args:
            image: The image to read (can be a file path or image array)
            detail (int): Detail level of the result
            paragraph (bool): Whether to combine text into paragraphs
            **kwargs: Additional arguments for the reader
            
        Returns:
            The OCR result
        """
        reader = OCRReader.get_instance()
        return reader.readtext(image, detail=detail, paragraph=paragraph, **kwargs)