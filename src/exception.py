#  exception handling code goes here
# sys is used to get the exception details and traceback module is used to get the stack trace of the exception
import sys 

def error_message_detail(error,err_detail:sys):
    _,_,exc_tb = err_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message
class CustomException(Exception):
    def __init__(self, message,err_detail:sys):
        self.message = error_message_detail(message, err_detail)
        super().__init__(self.message)
    def __str__(self):
        return self.message