#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Apt Pds 1
# Generated: Wed Jun 14 16:04:58 2017
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
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import sip
import sys
import time
from gnuradio import qtgui


class apt_pds_1(gr.top_block, Qt.QWidget):

    def __init__(self, sat_name='NOAA15'):
        gr.top_block.__init__(self, "Apt Pds 1")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Apt Pds 1")
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

        self.settings = Qt.QSettings("GNU Radio", "apt_pds_1")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.sat_name = sat_name

        ##################################################
        # Variables
        ##################################################
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y%m%d_%H%M%S.%f" )+'_UTC'
        self.samp_rate = samp_rate = 250000
        self.sarsat_fn = sarsat_fn = "{:s}_SARSAT_{:s}_{:s}k.fc32".format(sat_name, ts_str, str(int(samp_rate)/1000))
        self.apt_fn = apt_fn = "{:s}_APT_{:s}_{:s}k.fc32".format(sat_name, ts_str, str(int(samp_rate)/1000))
        self.sarsat_gain = sarsat_gain = 20
        self.sarsat_freq = sarsat_freq = 1544.5e6
        self.sarsat_fp = sarsat_fp = "/mnt/usbhdd/{:s}".format(sarsat_fn)
        self.apt_gain = apt_gain = 20
        self.apt_freq = apt_freq = 137.62e6
        self.apt_fp = apt_fp = "/mnt/usbhdd/{:s}".format(apt_fn)

        ##################################################
        # Blocks
        ##################################################
        self._sarsat_gain_tool_bar = Qt.QToolBar(self)
        self._sarsat_gain_tool_bar.addWidget(Qt.QLabel("sarsat_gain"+": "))
        self._sarsat_gain_line_edit = Qt.QLineEdit(str(self.sarsat_gain))
        self._sarsat_gain_tool_bar.addWidget(self._sarsat_gain_line_edit)
        self._sarsat_gain_line_edit.returnPressed.connect(
        	lambda: self.set_sarsat_gain(eng_notation.str_to_num(str(self._sarsat_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._sarsat_gain_tool_bar, 0,0,1,1)
        self._sarsat_freq_tool_bar = Qt.QToolBar(self)
        self._sarsat_freq_tool_bar.addWidget(Qt.QLabel("sarsat_freq"+": "))
        self._sarsat_freq_line_edit = Qt.QLineEdit(str(self.sarsat_freq))
        self._sarsat_freq_tool_bar.addWidget(self._sarsat_freq_line_edit)
        self._sarsat_freq_line_edit.returnPressed.connect(
        	lambda: self.set_sarsat_freq(eng_notation.str_to_num(str(self._sarsat_freq_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._sarsat_freq_tool_bar)
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
        self.uhd_usrp_source_0.set_center_freq(apt_freq, 0)
        self.uhd_usrp_source_0.set_gain(apt_gain, 0)
        self.uhd_usrp_source_0.set_antenna('TX/RX', 0)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"NOAA APT", #name
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
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"SARSAT", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0.set_y_axis(-120, -40)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + 'rtl=SARSAT' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(sarsat_freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(2, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(sarsat_gain, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.blocks_file_sink_1_0 = blocks.file_sink(gr.sizeof_gr_complex*1, apt_fp, False)
        self.blocks_file_sink_1_0.set_unbuffered(False)
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_gr_complex*1, sarsat_fp, False)
        self.blocks_file_sink_1.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.osmosdr_source_0, 0), (self.blocks_file_sink_1, 0))
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_file_sink_1_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_freq_sink_x_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "apt_pds_1")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sat_name(self):
        return self.sat_name

    def set_sat_name(self, sat_name):
        self.sat_name = sat_name
        self.set_sarsat_fn("{:s}_SARSAT_{:s}_{:s}k.fc32".format(self.sat_name, self.ts_str, str(int(self.samp_rate)/1000)))
        self.set_apt_fn("{:s}_APT_{:s}_{:s}k.fc32".format(self.sat_name, self.ts_str, str(int(self.samp_rate)/1000)))

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_sarsat_fn("{:s}_SARSAT_{:s}_{:s}k.fc32".format(self.sat_name, self.ts_str, str(int(self.samp_rate)/1000)))
        self.set_apt_fn("{:s}_APT_{:s}_{:s}k.fc32".format(self.sat_name, self.ts_str, str(int(self.samp_rate)/1000)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.set_sarsat_fn("{:s}_SARSAT_{:s}_{:s}k.fc32".format(self.sat_name, self.ts_str, str(int(self.samp_rate)/1000)))
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.set_apt_fn("{:s}_APT_{:s}_{:s}k.fc32".format(self.sat_name, self.ts_str, str(int(self.samp_rate)/1000)))

    def get_sarsat_fn(self):
        return self.sarsat_fn

    def set_sarsat_fn(self, sarsat_fn):
        self.sarsat_fn = sarsat_fn
        self.set_sarsat_fp("/mnt/usbhdd/{:s}".format(self.sarsat_fn))

    def get_apt_fn(self):
        return self.apt_fn

    def set_apt_fn(self, apt_fn):
        self.apt_fn = apt_fn
        self.set_apt_fp("/mnt/usbhdd/{:s}".format(self.apt_fn))

    def get_sarsat_gain(self):
        return self.sarsat_gain

    def set_sarsat_gain(self, sarsat_gain):
        self.sarsat_gain = sarsat_gain
        Qt.QMetaObject.invokeMethod(self._sarsat_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.sarsat_gain)))
        self.osmosdr_source_0.set_gain(self.sarsat_gain, 0)

    def get_sarsat_freq(self):
        return self.sarsat_freq

    def set_sarsat_freq(self, sarsat_freq):
        self.sarsat_freq = sarsat_freq
        Qt.QMetaObject.invokeMethod(self._sarsat_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.sarsat_freq)))
        self.osmosdr_source_0.set_center_freq(self.sarsat_freq, 0)

    def get_sarsat_fp(self):
        return self.sarsat_fp

    def set_sarsat_fp(self, sarsat_fp):
        self.sarsat_fp = sarsat_fp
        self.blocks_file_sink_1.open(self.sarsat_fp)

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
        self.uhd_usrp_source_0.set_center_freq(self.apt_freq, 0)

    def get_apt_fp(self):
        return self.apt_fp

    def set_apt_fp(self, apt_fp):
        self.apt_fp = apt_fp
        self.blocks_file_sink_1_0.open(self.apt_fp)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "-s", "--sat-name", dest="sat_name", type="string", default='NOAA15',
        help="Set sat_name [default=%default]")
    return parser


def main(top_block_cls=apt_pds_1, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(sat_name=options.sat_name)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
