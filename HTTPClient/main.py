import fire
import requests
import formatters
from colorama import Fore

def printResults(response):
	print("Status: " + formatters.formatStatusCode(response.status_code) + "\n")
	print(Fore.CYAN + "####### Headers ######" + Fore.RESET + "\n")
	print(formatters.formatHeaders(response.headers))
	print(Fore.CYAN + "####### Body ######" + Fore.RESET + "\n")
	encodeResponse = response.encoding
	print(response.content.decode(encodeResponse))


class httpMethodsCommands:
	def get(self, url, body={}, headers={}, params={}):
		response = requests.get(url, data=body, headers=headers, params=params)
		print(response.url)
		printResults(response)

	def post(self, url, body={}, headers={}, params={}):
		response = requests.post(url, data=body, headers=headers, params=params)
		printResults(response)

	def put(self, url, body={}, headers={}, params={}):
		response = requests.put(url, data=body, headers=headers, params=params)
		printResults(response)

	def delete(self, url, body={}, headers={}, params={}):
		response = requests.delete(url, data=body, headers=headers, params=params)
		printResults(response)

if __name__ == "__main__":
	fire.Fire(
		httpMethodsCommands,
		)
