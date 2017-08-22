#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Uhf Record Gui
# Generated: Tue Aug 22 16:32:28 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from datetime import datetime as dt; import string
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
import time
from gnuradio import qtgui


class uhf_record_gui(gr.top_block, Qt.QWidget):

    def __init__(self, gs_name='GS1', sat_name='NOAA15', sig_name='SIGNAL', freq=435.85e6, gain=30):
        gr.top_block.__init__(self, "Uhf Record Gui")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Uhf Record Gui")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "uhf_record_gui")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.gs_name = gs_name
        self.sat_name = sat_name
        self.sig_name = sig_name
        self.freq = freq
        self.gain = gain

        ##################################################
        # Variables
        ##################################################
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y%m%d_%H%M%S.%f" )+'_UTC'
        self.samp_rate = samp_rate = 250e3
        self.apt_fn = apt_fn = "{:s}_{:s}_{:s}_{:s}_{:s}k.fc32".format(gs_name, sat_name, sig_name, ts_str, str(int(samp_rate)/1000))
        self.apt_gain = apt_gain = gain
        self.apt_freq = apt_freq = freq
        self.apt_fp = apt_fp = "/mnt/usbhdd/{:s}".format(apt_fn)

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_tool_bar = Qt.QToolBar(self)
        self._samp_rate_tool_bar.addWidget(Qt.QLabel("samp_rate"+": "))
        self._samp_rate_line_edit = Qt.QLineEdit(str(self.samp_rate))
        self._samp_rate_tool_bar.addWidget(self._samp_rate_line_edit)
        self._samp_rate_line_edit.returnPressed.connect(
        	lambda: self.set_samp_rate(eng_notation.str_to_num(str(self._samp_rate_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._samp_rate_tool_bar)
        self._apt_gain_tool_bar = Qt.QToolBar(self)
        self._apt_gain_tool_bar.addWidget(Qt.QLabel("apt_gain"+": "))
        self._apt_gain_line_edit = Qt.QLineEdit(str(self.apt_gain))
        self._apt_gain_tool_bar.addWidget(self._apt_gain_line_edit)
        self._apt_gain_line_edit.returnPressed.connect(
        	lambda: self.set_apt_gain(eng_notation.str_to_num(str(self._apt_gain_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._apt_gain_tool_bar)
        self._apt_freq_tool_bar = Qt.QToolBar(self)
        self._apt_freq_tool_bar.addWidget(Qt.QLabel("apt_freq"+": "))
        self._apt_freq_line_edit = Qt.QLineEdit(str(self.apt_freq))
        self._apt_freq_tool_bar.addWidget(self._apt_freq_line_edit)
        self._apt_freq_line_edit.returnPressed.connect(
        	lambda: self.set_apt_freq(eng_notation.str_to_num(str(self._apt_freq_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._apt_freq_tool_bar)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_clock_source('gpsdo', 0)
        self.uhd_usrp_source_0.set_time_source('gpsdo', 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(apt_freq, samp_rate/2), 0)
        self.uhd_usrp_source_0.set_gain(apt_gain, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"FO-29 Transponder", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, -40)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"FO-29 Transponder", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-120, -40)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.blocks_file_sink_1_0 = blocks.file_sink(gr.sizeof_gr_complex*1, apt_fp, False)
        self.blocks_file_sink_1_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_file_sink_1_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_waterfall_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "uhf_record_gui")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_gs_name(self):
        return self.gs_name

    def set_gs_name(self, gs_name):
        self.gs_name = gs_name
        self.set_apt_fn("{:s}_{:s}_{:s}_{:s}_{:s}k.fc32".format(self.gs_name, self.sat_name, self.sig_name, self.ts_str, str(int(self.samp_rate)/1000)))

    def get_sat_name(self):
        return self.sat_name

    def set_sat_name(self, sat_name):
        self.sat_name = sat_name
        self.set_apt_fn("{:s}_{:s}_{:s}_{:s}_{:s}k.fc32".format(self.gs_name, self.sat_name, self.sig_name, self.ts_str, str(int(self.samp_rate)/1000)))

    def get_sig_name(self):
        return self.sig_name

    def set_sig_name(self, sig_name):
        self.sig_name = sig_name
        self.set_apt_fn("{:s}_{:s}_{:s}_{:s}_{:s}k.fc32".format(self.gs_name, self.sat_name, self.sig_name, self.ts_str, str(int(self.samp_rate)/1000)))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.set_apt_freq(self.freq)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.set_apt_gain(self.gain)

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_apt_fn("{:s}_{:s}_{:s}_{:s}_{:s}k.fc32".format(self.gs_name, self.sat_name, self.sig_name, self.ts_str, str(int(self.samp_rate)/1000)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.apt_freq, self.samp_rate/2), 0)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.set_apt_fn("{:s}_{:s}_{:s}_{:s}_{:s}k.fc32".format(self.gs_name, self.sat_name, self.sig_name, self.ts_str, str(int(self.samp_rate)/1000)))

    def get_apt_fn(self):
        return self.apt_fn

    def set_apt_fn(self, apt_fn):
        self.apt_fn = apt_fn
        self.set_apt_fp("/mnt/usbhdd/{:s}".format(self.apt_fn))

    def get_apt_gain(self):
        return self.apt_gain

    def set_apt_gain(self, apt_gain):
        self.apt_gain = apt_gain
        Qt.QMetaObject.invokeMethod(self._apt_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.apt_gain)))
        self.uhd_usrp_source_0.set_gain(self.apt_gain, 0)


    def get_apt_freq(self):
        return self.apt_freq

    def set_apt_freq(self, apt_freq):
        self.apt_freq = apt_freq
        Qt.QMetaObject.invokeMethod(self._apt_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.apt_freq)))
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.apt_freq, self.samp_rate/2), 0)

    def get_apt_fp(self):
        return self.apt_fp

    def set_apt_fp(self, apt_fp):
        self.apt_fp = apt_fp
        self.blocks_file_sink_1_0.open(self.apt_fp)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--gs-name", dest="gs_name", type="string", default='GS1',
        help="Set gs_name [default=%default]")
    parser.add_option(
        "", "--sat-name", dest="sat_name", type="string", default='NOAA15',
        help="Set sat_name [default=%default]")
    parser.add_option(
        "", "--sig-name", dest="sig_name", type="string", default='SIGNAL',
        help="Set sig_name [default=%default]")
    parser.add_option(
        "", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(435.85e6),
        help="Set freq [default=%default]")
    parser.add_option(
        "", "--gain", dest="gain", type="eng_float", default=eng_notation.num_to_str(30),
        help="Set gain [default=%default]")
    return parser


def main(top_block_cls=uhf_record_gui, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(gs_name=options.gs_name, sat_name=options.sat_name, sig_name=options.sig_name, freq=options.freq, gain=options.gain)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
