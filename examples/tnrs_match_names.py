#!/usr/bin/env python3
import json
import sys

from opentree import OTCommandLineTool

cli = OTCommandLineTool(usage='Look up the OTT IDs for a set of names')
cli.parser.add_argument("names", nargs="+", help="names to match")
cli.parser.add_argument("--context-name", default=None,
                        help='If you know the named Open Tree name searching index, you can supply it here ' 
                             'to limit your search to only a subset of the taxonomny.')
cli.parser.add_argument("--do-approximate-matching", action="store_true",
                        help='Enables fuzzy matching')
cli.parser.add_argument("--include-suppressed", action="store_true",
                        help='Return taxa that are normally suppressed from TNRS '
                             'results. See https://github.com/OpenTreeOfLife/reference-taxonomy/wiki/Taxon-flags#flags-leading-to-taxa-being-unavailable-for-tnrs')
OT, args = cli.parse_cli()

print(repr(args))
output = OT.tnrs_match(args.names,
                       context_name=args.context_name,
                       do_approximate_matching=args.do_approximate_matching,
                       include_suppressed=args.include_suppressed)

print(json.dumps(output.response_dict, indent=2, sort_keys=True))
