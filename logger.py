class logger:
    def log(self,message,message_type = "info"):
        if message_type == "error":
            print(f"[error] {message}")
        elif message_type == "warning":
            print(f"[warning] {message}")
        else:
            print(f"[info] {message}")
logger = logger()
logger.log("this is a message")
logger.log("this is a warning message","warning")
logger.log("this is an error message","error")
