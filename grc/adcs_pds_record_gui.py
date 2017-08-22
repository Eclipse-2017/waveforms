#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Adcs Pds Record Gui
# Generated: Tue Aug 22 16:50:38 2017
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


class adcs_pds_record_gui(gr.top_block, Qt.QWidget):

    def __init__(self, adcs_freq=465.9875e6, adcs_gain=25, gs_name='GS1', sarsat_freq=1544.5e6, sarsat_gain=25, sat_name='METOPB'):
        gr.top_block.__init__(self, "Adcs Pds Record Gui")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Adcs Pds Record Gui")
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

        self.settings = Qt.QSettings("GNU Radio", "adcs_pds_record_gui")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.adcs_freq = adcs_freq
        self.adcs_gain = adcs_gain
        self.gs_name = gs_name
        self.sarsat_freq = sarsat_freq
        self.sarsat_gain = sarsat_gain
        self.sat_name = sat_name

        ##################################################
        # Variables
        ##################################################
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y%m%d_%H%M%S.%f" )+'_UTC'
        self.samp_rate = samp_rate = 1000000
        self.decim = decim = 4
        self.sarsat_fn = sarsat_fn = "{:s}_{:s}_SARSAT_{:s}_{:s}k.fc32".format(gs_name, sat_name, ts_str, str(int(samp_rate/decim)/1000))
        self.adcs_fn = adcs_fn = "{:s}_{:s}_ADCS_{:s}_{:s}k.fc32".format(gs_name, sat_name, ts_str, str(int(samp_rate/decim)/1000))
        self.sarsat_fp = sarsat_fp = "/mnt/usbhdd/{:s}".format(sarsat_fn)
        self.adcs_fp = adcs_fp = "/mnt/usbhdd/{:s}".format(adcs_fn)

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_clock_source('gpsdo', 0)
        self.uhd_usrp_source_0.set_time_source('gpsdo', 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate/decim)
        self.uhd_usrp_source_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(adcs_freq, (samp_rate/decim)/2), 0)
        self.uhd_usrp_source_0.set_gain(adcs_gain, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decim,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim, #bw
        	"ADCS - UHF", #name
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

        self.blocks_file_sink_1_0 = blocks.file_sink(gr.sizeof_gr_complex*1, adcs_fp, False)
        self.blocks_file_sink_1_0.set_unbuffered(False)
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_gr_complex*1, sarsat_fp, False)
        self.blocks_file_sink_1.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.osmosdr_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_file_sink_1, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_file_sink_1_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_freq_sink_x_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "adcs_pds_record_gui")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_adcs_freq(self):
        return self.adcs_freq

    def set_adcs_freq(self, adcs_freq):
        self.adcs_freq = adcs_freq
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.adcs_freq, (self.samp_rate/self.decim)/2), 0)

    def get_adcs_gain(self):
        return self.adcs_gain

    def set_adcs_gain(self, adcs_gain):
        self.adcs_gain = adcs_gain
        self.uhd_usrp_source_0.set_gain(self.adcs_gain, 0)


    def get_gs_name(self):
        return self.gs_name

    def set_gs_name(self, gs_name):
        self.gs_name = gs_name
        self.set_sarsat_fn("{:s}_{:s}_SARSAT_{:s}_{:s}k.fc32".format(self.gs_name, self.sat_name, self.ts_str, str(int(self.samp_rate/self.decim)/1000)))
        self.set_adcs_fn("{:s}_{:s}_ADCS_{:s}_{:s}k.fc32".format(self.gs_name, self.sat_name, self.ts_str, str(int(self.samp_rate/self.decim)/1000)))

    def get_sarsat_freq(self):
        return self.sarsat_freq

    def set_sarsat_freq(self, sarsat_freq):
        self.sarsat_freq = sarsat_freq
        self.osmosdr_source_0.set_center_freq(self.sarsat_freq, 0)

    def get_sarsat_gain(self):
        return self.sarsat_gain

    def set_sarsat_gain(self, sarsat_gain):
        self.sarsat_gain = sarsat_gain
        self.osmosdr_source_0.set_gain(self.sarsat_gain, 0)

    def get_sat_name(self):
        return self.sat_name

    def set_sat_name(self, sat_name):
        self.sat_name = sat_name
        self.set_sarsat_fn("{:s}_{:s}_SARSAT_{:s}_{:s}k.fc32".format(self.gs_name, self.sat_name, self.ts_str, str(int(self.samp_rate/self.decim)/1000)))
        self.set_adcs_fn("{:s}_{:s}_ADCS_{:s}_{:s}k.fc32".format(self.gs_name, self.sat_name, self.ts_str, str(int(self.samp_rate/self.decim)/1000)))

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_sarsat_fn("{:s}_{:s}_SARSAT_{:s}_{:s}k.fc32".format(self.gs_name, self.sat_name, self.ts_str, str(int(self.samp_rate/self.decim)/1000)))
        self.set_adcs_fn("{:s}_{:s}_ADCS_{:s}_{:s}k.fc32".format(self.gs_name, self.sat_name, self.ts_str, str(int(self.samp_rate/self.decim)/1000)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate/self.decim)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.adcs_freq, (self.samp_rate/self.decim)/2), 0)
        self.set_sarsat_fn("{:s}_{:s}_SARSAT_{:s}_{:s}k.fc32".format(self.gs_name, self.sat_name, self.ts_str, str(int(self.samp_rate/self.decim)/1000)))
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.set_adcs_fn("{:s}_{:s}_ADCS_{:s}_{:s}k.fc32".format(self.gs_name, self.sat_name, self.ts_str, str(int(self.samp_rate/self.decim)/1000)))

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate/self.decim)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.adcs_freq, (self.samp_rate/self.decim)/2), 0)
        self.set_sarsat_fn("{:s}_{:s}_SARSAT_{:s}_{:s}k.fc32".format(self.gs_name, self.sat_name, self.ts_str, str(int(self.samp_rate/self.decim)/1000)))
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.set_adcs_fn("{:s}_{:s}_ADCS_{:s}_{:s}k.fc32".format(self.gs_name, self.sat_name, self.ts_str, str(int(self.samp_rate/self.decim)/1000)))

    def get_sarsat_fn(self):
        return self.sarsat_fn

    def set_sarsat_fn(self, sarsat_fn):
        self.sarsat_fn = sarsat_fn
        self.set_sarsat_fp("/mnt/usbhdd/{:s}".format(self.sarsat_fn))

    def get_adcs_fn(self):
        return self.adcs_fn

    def set_adcs_fn(self, adcs_fn):
        self.adcs_fn = adcs_fn
        self.set_adcs_fp("/mnt/usbhdd/{:s}".format(self.adcs_fn))

    def get_sarsat_fp(self):
        return self.sarsat_fp

    def set_sarsat_fp(self, sarsat_fp):
        self.sarsat_fp = sarsat_fp
        self.blocks_file_sink_1.open(self.sarsat_fp)

    def get_adcs_fp(self):
        return self.adcs_fp

    def set_adcs_fp(self, adcs_fp):
        self.adcs_fp = adcs_fp
        self.blocks_file_sink_1_0.open(self.adcs_fp)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--adcs-freq", dest="adcs_freq", type="eng_float", default=eng_notation.num_to_str(465.9875e6),
        help="Set adcs_freq [default=%default]")
    parser.add_option(
        "", "--adcs-gain", dest="adcs_gain", type="eng_float", default=eng_notation.num_to_str(25),
        help="Set adcs_gain [default=%default]")
    parser.add_option(
        "", "--gs-name", dest="gs_name", type="string", default='GS1',
        help="Set gs_name [default=%default]")
    parser.add_option(
        "", "--sarsat-freq", dest="sarsat_freq", type="eng_float", default=eng_notation.num_to_str(1544.5e6),
        help="Set sarsat_freq [default=%default]")
    parser.add_option(
        "", "--sarsat-gain", dest="sarsat_gain", type="eng_float", default=eng_notation.num_to_str(25),
        help="Set sarsat_gain [default=%default]")
    parser.add_option(
        "", "--sat-name", dest="sat_name", type="string", default='METOPB',
        help="Set sat_name [default=%default]")
    return parser


def main(top_block_cls=adcs_pds_record_gui, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(adcs_freq=options.adcs_freq, adcs_gain=options.adcs_gain, gs_name=options.gs_name, sarsat_freq=options.sarsat_freq, sarsat_gain=options.sarsat_gain, sat_name=options.sat_name)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
