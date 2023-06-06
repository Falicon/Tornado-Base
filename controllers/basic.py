import tornado.web

import simplejson as json

class BaseHandler(tornado.web.RequestHandler):

  ########################################
  # GET CURRENT USER
  #   returns value stored in account cookie; used to check if user is logged in
  ########################################
  def get_current_user(self):
    return self.get_secure_cookie("account")

  ########################################
  # API RESPONSE
  #   wrapper function to return a more useful response to the end user
  ########################################
  def api_response(self, data):
    # return an api response in the proper output format with status_code == 200
    self.write_api_response(data, 200, "OK")

  ########################################
  # ERROR
  #   rendered when the application hits a python error
  ########################################
  def error(self, status_code, status_txt, data=None):
    # return an api error in the proper output format
    self.write_api_response(status_code=status_code, status_txt=status_txt, data=data)

  ########################################
  # WRITE API RESPONSE
  #   internal method used to format a json response (instead of returning an HTML document)
  ########################################
  def write_api_response(self, data, status_code, status_txt):
    # return an api error based on the appropriate request format (ie: json)
    format = self.get_argument('format', 'json')
    callback = self.get_argument('callback', None)
    if format not in ["json"]:
      status_code = 500
      status_txt = "INVALID_ARG_FORMAT"
      data = None
      format = "json"

    response = {'status_code':status_code, 'status_txt':status_txt, 'data':data}

    if format == "json":
      data = json.dumps(response)
      if callback:
        self.set_header("Content-Type", "application/javascript; charset=utf-8")
        self.write('%s(%s)' % (callback, data))
      else:
        self.set_header("Content-Type", "application/json; charset=utf-8")
        self.write(data)

      self.finish()
