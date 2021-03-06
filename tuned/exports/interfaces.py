class ExportableInterface(object):
	pass

class ExporterInterface(object):
	def export(self, method, in_signature, out_signature):
		# to be overriden by concrete implementation
		raise NotImplemented()

	def signal(self, method, out_signature):
		# to be overriden by concrete implementation
		raise NotImplemented()

	def send_signal(self, signal, *args, **kwargs):
		# to be overriden by concrete implementation
		raise NotImplemented()

	def start(self):
		raise NotImplemented()

	def stop(self):
		raise NotImplemented()
