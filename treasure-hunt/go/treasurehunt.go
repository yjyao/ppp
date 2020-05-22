package main

import (
	"fmt"
	"image"
)

type Board [][]image.Point

func MakeCoord(c int) image.Point {
	return image.Point{c%10 - 1, c/10 - 1}
}

func MakeBoard(b [][]int) Board {
	nb := make([][]image.Point, len(b))
	for y, r := range b {
		nb[y] = make([]image.Point, len(r))
		for x, c := range r {
			nb[y][x] = MakeCoord(c)
		}
	}
	return Board(nb)
}

func Walk(b Board, s image.Point) []image.Point {
	ps := []image.Point{}
	p := s
	for {
		ps = append(ps, p)
		np := b[p.Y][p.X]
		if np == p {
			break
		}
		p = np
	}
	return ps
}

func main() {
	board := [][]int{
		{34, 21, 32, 41, 25},
		{14, 42, 43, 14, 31},
		{54, 45, 52, 42, 23},
		{33, 15, 51, 31, 35},
		{21, 52, 33, 13, 23},
	}
	for _, p := range Walk(MakeBoard(board), image.Point{0, 0}) {
		fmt.Println((p.Y+1)*10 + (p.X + 1))
	}
}
