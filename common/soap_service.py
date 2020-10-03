from suds.client import Client


class SoapService:

    url: str = 'http://www.dneonline.com/calculator.asmx?WSDL'

    def get_time_remaining(self, time_worked: int, estimated_time: float) -> int:
        estimated_time = round(estimated_time)
        client = Client(url=self.url)
        response = client.service.Subtract(estimated_time, time_worked)
        return response
