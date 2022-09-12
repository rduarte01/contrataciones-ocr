from services import *

contrataciones_services = Contrataciones_services()
ocrmypdf = Ocrmypdf_service() 
pdf2image = Pdf2image_services()

def main():
  """
  Part #1 : get data 
  """
  response = contrataciones_services.get_data(module="contracts", id="LC-12006-19-170106")

  filename = "metadata"

  url = response["contracts"][0]["documents"][0]["url"]
  """
  Part #2 : download file to files directory
  """
  contrataciones_services.downloadFile(url,f"{filename}_original.pdf")
  """
  Part #3 : preproced data with ocrmypdf
  """
  ocrmypdf.scanned_pdf_converter(f"{filename}_original.pdf",f"{filename}_ocrmypdf.pdf")
  """
  Part #4 : convert pdf to text
  """
  pdf2image.pdf_to_text(filename)



if __name__ == "__main__":
	# We only want to run this if it's directly executed!
	main()
