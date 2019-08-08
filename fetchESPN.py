# Use XML DOM to parse ESPN "Top Headlines" RSS Feed

import xml.dom.minidom
import requests

def main():
    # retrieve the XML data using the requests library
    url ="https://www.espn.com/espn/rss/news"
    result = requests.get(url)
    
    # parse the returned content into a DOM structure
    domtree = xml.dom.minidom.parseString(result.text)
    rootnode = domtree.documentElement 

    # print some feed metadata
    print("Root element: {0}".format(rootnode.nodeName))
    print("Version: {0}".format(rootnode.getAttribute('version')))

    # pull the items
    items = domtree.getElementsByTagName("item")
    print("There are {0} items:".format(items.length))

    # iterate over the items
    for item in items: 
        print("{0}".format(item.firstChild.firstChild.nodeValue))

if __name__ == "__main__":
    main()
