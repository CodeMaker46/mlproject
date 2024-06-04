import sys
import logging
def error_message_detail(error,error_detail:sys):
    '''3 details deta hai phli 2 kam ki nhi hoti hai'''
    _,_,exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format()
    file_name,exc_tb.tb_lineno,str(error)
    return error_message


class CustomException(Exception):
    def _init_(self,error_message,error_details:sys):
        super._init_(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def str(self):
        return self.error_message

_name_main = "_main_"
if _name_=="_main_":

    try:
        a=1/0 
    except Exception as e :
        logging.info("Divide by zero")
        raise CustomException(e,sys)