
# /home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_yacctab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\x03\x1bS\x1d\xbf\x0c\xbe\xbaa\xfe\xbf\xb7G\x8d%\xb2'
    
_lr_action_items = {'false':([36,48,],[39,39,]),'JDSWINGOBJECT':([8,21,25,29,31,34,38,44,47,49,],[11,11,-6,-3,-5,-4,-7,11,-8,11,]),'TEXT':([36,48,],[41,41,]),'SYMBOL':([2,10,27,30,33,35,37,39,40,41,42,43,44,45,46,50,51,52,53,54,],[3,28,28,-23,28,-22,28,-34,-28,-32,-31,-30,28,-33,-24,28,-25,-29,-27,-26,]),'GLOBAL':([4,5,],[7,7,]),'JDELLIPSE':([8,21,25,29,31,34,38,44,47,49,],[12,12,-6,-3,-5,-4,-7,12,-8,12,]),'LBRACKET':([2,3,7,11,12,13,14,15,16,17,18,19,20,22,23,24,26,36,],[4,5,10,-15,-13,-17,-11,-18,-19,-9,-12,-14,-20,-16,33,-10,-21,44,]),'JDPOLYLINE':([8,21,25,29,31,34,38,44,47,49,],[13,13,-6,-3,-5,-4,-7,13,-8,13,]),'JDSPLINE':([8,21,25,29,31,34,38,44,47,49,],[26,26,-6,-3,-5,-4,-7,26,-8,26,]),'JDIMAGE':([8,21,25,29,31,34,38,44,47,49,],[15,15,-6,-3,-5,-4,-7,15,-8,15,]),'JDAXIS':([8,21,25,29,31,34,38,44,47,49,],[16,16,-6,-3,-5,-4,-7,16,-8,16,]),'JDLINE':([8,21,25,29,31,34,38,44,47,49,],[17,17,-6,-3,-5,-4,-7,17,-8,17,]),'JDGROUP':([8,21,25,29,31,34,38,44,47,49,],[18,18,-6,-3,-5,-4,-7,18,-8,18,]),'COMMA':([39,40,41,42,43,45,52,],[-34,48,-32,-31,-30,-33,-29,]),'JDBAR':([8,21,25,29,31,34,38,44,47,49,],[19,19,-6,-3,-5,-4,-7,19,-8,19,]),'JDSLIDER':([8,21,25,29,31,34,38,44,47,49,],[20,20,-6,-3,-5,-4,-7,20,-8,20,]),'$end':([1,9,32,],[0,-2,-1,]),'JDLABEL':([8,21,25,29,31,34,38,44,47,49,],[22,22,-6,-3,-5,-4,-7,22,-8,22,]),'NUMBER':([36,48,],[42,42,]),'true':([36,48,],[45,45,]),'JDRECTANGLE':([8,21,25,29,31,34,38,44,47,49,],[24,24,-6,-3,-5,-4,-7,24,-8,24,]),'JDFILE':([0,],[2,]),'RBRACKET':([6,10,21,25,27,29,30,31,33,34,35,37,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53,54,],[9,29,32,-6,34,-3,-23,-5,38,-4,-22,47,-7,-34,-28,-32,-31,-30,51,-33,-24,-8,53,54,-25,-29,-27,-26,]),'TWOP':([28,],[36,]),'JDROUNDRECTANGLE':([8,21,25,29,31,34,38,44,47,49,],[14,14,-6,-3,-5,-4,-7,14,-8,14,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'obj':([8,21,44,49,],[23,23,23,23,]),'parameter_list':([10,33,44,],[27,37,50,]),'element_list':([8,44,],[21,49,]),'value_list':([36,],[40,]),'global':([4,5,],[6,8,]),'value':([36,48,],[43,52,]),'element':([8,21,44,49,],[25,31,25,31,]),'param_value':([36,],[46,]),'parameter':([10,27,33,37,44,50,],[30,35,30,35,30,35,]),'jdfile':([0,],[1,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> jdfile","S'",1,None,None,None),
  ('jdfile -> JDFILE SYMBOL LBRACKET global element_list RBRACKET','jdfile',6,'p_jdfile','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',107),
  ('jdfile -> JDFILE LBRACKET global RBRACKET','jdfile',4,'p_jdfile_empty','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',115),
  ('global -> GLOBAL LBRACKET RBRACKET','global',3,'p_global','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',123),
  ('global -> GLOBAL LBRACKET parameter_list RBRACKET','global',4,'p_global','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',124),
  ('element_list -> element_list element','element_list',2,'p_element_list','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',131),
  ('element_list -> element','element_list',1,'p_element','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',138),
  ('element -> obj LBRACKET RBRACKET','element',3,'p_single_element','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',142),
  ('element -> obj LBRACKET parameter_list RBRACKET','element',4,'p_single_element','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',143),
  ('obj -> JDLINE','obj',1,'p_obj','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',191),
  ('obj -> JDRECTANGLE','obj',1,'p_obj','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',192),
  ('obj -> JDROUNDRECTANGLE','obj',1,'p_obj','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',193),
  ('obj -> JDGROUP','obj',1,'p_obj','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',194),
  ('obj -> JDELLIPSE','obj',1,'p_obj','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',195),
  ('obj -> JDBAR','obj',1,'p_obj','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',196),
  ('obj -> JDSWINGOBJECT','obj',1,'p_obj','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',197),
  ('obj -> JDLABEL','obj',1,'p_obj','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',198),
  ('obj -> JDPOLYLINE','obj',1,'p_obj','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',199),
  ('obj -> JDIMAGE','obj',1,'p_obj','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',200),
  ('obj -> JDAXIS','obj',1,'p_obj','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',201),
  ('obj -> JDSLIDER','obj',1,'p_obj','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',202),
  ('obj -> JDSPLINE','obj',1,'p_obj','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',203),
  ('parameter_list -> parameter_list parameter','parameter_list',2,'p_parameter_list','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',207),
  ('parameter_list -> parameter','parameter_list',1,'p_parameter','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',212),
  ('parameter -> SYMBOL TWOP param_value','parameter',3,'p_single_parameter','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',216),
  ('parameter -> SYMBOL TWOP LBRACKET RBRACKET','parameter',4,'p_complex_parameter','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',225),
  ('parameter -> SYMBOL TWOP LBRACKET parameter_list RBRACKET','parameter',5,'p_complex_parameter','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',226),
  ('parameter -> SYMBOL TWOP LBRACKET element_list RBRACKET','parameter',5,'p_complex_parameter','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',227),
  ('param_value -> value_list','param_value',1,'p_param_value_number_list','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',235),
  ('value_list -> value_list COMMA value','value_list',3,'p_value_list','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',242),
  ('value_list -> value','value_list',1,'p_value_list_value','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',246),
  ('value -> NUMBER','value',1,'p_value_number','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',250),
  ('value -> TEXT','value',1,'p_value_text','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',254),
  ('value -> true','value',1,'p_value_bool','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',258),
  ('value -> false','value',1,'p_value_bool','/home/tango-cs/taurus/taurus-3.6.0/lib/taurus/qt/qtgui/graphic/jdraw/jdraw_parser.py',259),
]
