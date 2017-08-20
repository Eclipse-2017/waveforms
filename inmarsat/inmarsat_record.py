#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Inmarsat Record
# Generated: Sat Aug 19 20:18:46 2017
##################################################

from datetime import datetime as dt; import string
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import time
import sys


class inmarsat_record(gr.top_block):

    def __init__(self, sat_name='4F3', gs_name='GS1', rx_gain=25, rx_freq=1539.96e6):
        gr.top_block.__init__(self, "Inmarsat Record")

        ##################################################
        # Parameters
        ##################################################
        self.sat_name = sat_name
        self.gs_name = gs_name
        self.rx_gain = rx_gain
        self.rx_freq = rx_freq

        ##################################################
        # Variables
        ##################################################
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y%m%d_%H%M%S.%f" )+'_UTC'
        self.samp_rate = samp_rate = 1000000
        self.decim = decim = 4
        self.inmarsat_fn = inmarsat_fn = "{:s}_{:s}_{:s}_{:s}k.fc32".format(gs_name,sat_name, ts_str, str(int(samp_rate/decim)/1000))
        self.inmarsat_fp = inmarsat_fp = "/mnt/usbhdd/{:s}".format(inmarsat_fn)

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decim,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + 'rtl=INMARSAT' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(rx_freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(rx_gain, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_gr_complex*1, inmarsat_fp, False)
        self.blocks_file_sink_1.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.osmosdr_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_file_sink_1, 0))

    def get_sat_name(self):
        return self.sat_name

    def set_sat_name(self, sat_name):
        self.sat_name = sat_name
        self.set_inmarsat_fn("{:s}_{:s}_{:s}_{:s}k.fc32".format(self.gs_name,self.sat_name, self.ts_str, str(int(self.samp_rate/self.decim)/1000)))

    def get_gs_name(self):
        return self.gs_name

    def set_gs_name(self, gs_name):
        self.gs_name = gs_name
        self.set_inmarsat_fn("{:s}_{:s}_{:s}_{:s}k.fc32".format(self.gs_name,self.sat_name, self.ts_str, str(int(self.samp_rate/self.decim)/1000)))

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.osmosdr_source_0.set_gain(self.rx_gain, 0)
        self.osmosdr_source_0.set_gain(self.rx_gain, 1)

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        self.osmosdr_source_0.set_center_freq(self.rx_freq, 0)
        self.osmosdr_source_0.set_center_freq(self.rx_freq, 1)

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_inmarsat_fn("{:s}_{:s}_{:s}_{:s}k.fc32".format(self.gs_name,self.sat_name, self.ts_str, str(int(self.samp_rate/self.decim)/1000)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.set_inmarsat_fn("{:s}_{:s}_{:s}_{:s}k.fc32".format(self.gs_name,self.sat_name, self.ts_str, str(int(self.samp_rate/self.decim)/1000)))

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.set_inmarsat_fn("{:s}_{:s}_{:s}_{:s}k.fc32".format(self.gs_name,self.sat_name, self.ts_str, str(int(self.samp_rate/self.decim)/1000)))

    def get_inmarsat_fn(self):
        return self.inmarsat_fn

    def set_inmarsat_fn(self, inmarsat_fn):
        self.inmarsat_fn = inmarsat_fn
        self.set_inmarsat_fp("/mnt/usbhdd/{:s}".format(self.inmarsat_fn))

    def get_inmarsat_fp(self):
        return self.inmarsat_fp

    def set_inmarsat_fp(self, inmarsat_fp):
        self.inmarsat_fp = inmarsat_fp
        self.blocks_file_sink_1.open(self.inmarsat_fp)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "-s", "--sat-name", dest="sat_name", type="string", default='4F3',
        help="Set sat_name [default=%default]")
    parser.add_option(
        "-n", "--gs-name", dest="gs_name", type="string", default='GS1',
        help="Set gs_name [default=%default]")
    parser.add_option(
        "-g", "--rx-gain", dest="rx_gain", type="eng_float", default=eng_notation.num_to_str(25),
        help="Set rx_gain [default=%default]")
    parser.add_option(
        "-f", "--rx-freq", dest="rx_freq", type="eng_float", default=eng_notation.num_to_str(1539.96e6),
        help="Set rx_freq [default=%default]")
    return parser


def main(top_block_cls=inmarsat_record, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(sat_name=options.sat_name, gs_name=options.gs_name, rx_gain=options.rx_gain, rx_freq=options.rx_freq)
    tb.start()
    start_time = dt.utcnow()
    delta = 0
    while delta < 60.0:
        delta = (dt.utcnow() - start_time).total_seconds()
    sys.exit()
    tb.wait()


if __name__ == '__main__':
    main()
