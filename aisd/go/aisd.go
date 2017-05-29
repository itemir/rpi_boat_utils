/*
Copyright (c) 2017 Ilker Temir

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/

package main

import (
	"bufio"
	"flag"
	"fmt"
	"net"
	"os"
)

func send_messages(file_name string, pipe chan net.Conn) {
	ch := make(chan []byte)
	go func(ch chan []byte) {
		f, err := os.Open(file_name)
		if err != nil {
			fmt.Println("Cannot open file")
			os.Exit(1)
		}
		reader := bufio.NewReader(f)
		for {
			s, _, err := reader.ReadLine()
			if err != nil {
				close(ch)
				return
			}
			ch <- s
		}
	}(ch)

	conn_list := []net.Conn{}
	for {
		select {
		case conn := <-pipe:
			conn_list = append(conn_list, conn)
		default:
		}
		select {
		case message := <-ch:
			for _, conn := range conn_list {
				conn.Write(append(message, []byte("\n")...))
			}
		default:
		}
	}
}

func main() {
	var file_name string
	var port_number int
	flag.StringVar(&file_name, "file", "/dev/ttyUSB0",
		"File to read AIS messages from")
	flag.IntVar(&port_number, "port", 1920, "Port number")
	flag.Parse()

	pipe := make(chan net.Conn)
	go send_messages(file_name, pipe)

	port_string := fmt.Sprintf(":%d", port_number)
	ln, err := net.Listen("tcp", port_string)
	if err != nil {
		fmt.Println("Socket error")
		os.Exit(1)
	}

	fmt.Printf("Starting AIS daemon on port %d\n", port_number)
	for {
		conn, err := ln.Accept()
		if err != nil {
			fmt.Println("Socket error")
			os.Exit(1)
		}
		pipe <- conn
	}
}
