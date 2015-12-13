#!/usr/bin/env python
# -*- encode: utf-8 -*-

import sys
import json
import facebook


class Timeline:

    def __init__(self, token_file):
        with open(token_file, 'r') as f:
            token = json.load(f)['token']
            self.user_endpoint = facebook.GraphAPI(token['user_access'])
            self.page_endpoint = facebook.GraphAPI(token['page_access'])

    def post_me(self, msg):
        self.user_endpoint.put_object('me', 'feed', message=msg)
        print('posted to my timeline: %s' % msg)

    def post_page(self, msg):
        self.page_endpoint.put_wall_post(message=msg)
        print('posted to page timeline: %s' % msg)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('usage: %s token_file [me|page] message' % sys.argv[0])
        exit(1)
    try:
        timeline = Timeline(sys.argv[1])
        if sys.argv[2] == 'me':
            timeline.post_me(sys.argv[3])
        elif sys.argv[2] == 'page':
            timeline.post_page(sys.argv[3])
        else:
            print '%s is invalid' % sys.argv[2]
    except (IOError, facebook.GraphAPIError) as e:
        print e
        exit(9)
