// gcc jpuc1143-F.c -o jpuc1143-F


#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <time.h>


typedef struct cell {
	int edges;
	bool visited;
} Cell;

typedef struct printCell {
	int edges;
	Cell *cell;
} PrintCell;

typedef struct maze {
	int size;
	struct cell *cells;
} Maze;

typedef struct printMaze {
	int size;
	PrintCell *cells;
} PrintMaze;

typedef struct point {
	int x;
	int y;
} Point;

void printWall(int edges) {
	switch (edges) {
	case 0000:
		printf("╬");
		break;
	case 0001:
		printf("╣");
		break;
	case 0010:
		printf("╩");
		break;
	case 0011:
		printf("╗");
		break;
	case 0100:
		printf("╬");
		break;
	case 0101:
		printf("╬");
		break;
	default:
		printf("?");
		break;
	}
}

Point addPoints(Point a, Point b)
{
	return (Point) {
		.x = a.x + b.x,
		.y = a.y + b.y
	};
}

void connectCells(Cell *a, Cell *b, Point delta)
{
	if (delta.x == 1) {
		a->edges |= 0b0001;
		b->edges |= 0b1000;
	} else if (delta.x == -1) {
		a->edges |= 0b1000;
		b->edges |= 0b0001;
	} else if (delta.y == 1) {
		a->edges |= 0b0100;
		b->edges |= 0b0010;
	} else if (delta.y == -1) {
		a->edges |= 0b0010;
		b->edges |= 0b0100;
	}
}

Cell* getCell(Maze *maze, Point point)
{
	if (point.x >= 0 && point.x < maze->size
			&& point.y >= 0 && point.y < maze->size) {
		return maze->cells + maze->size * point.y + point.x;
	} else {
		return NULL;
	}

}

PrintCell* getPrintCell(PrintMaze *maze, Point point)
{
	if (point.x >= 0 && point.x < maze->size
			&& point.y >= 0 && point.y < maze->size) {
		return maze->cells + maze->size * point.y + point.x;
	} else {
		return NULL;
	}

}

Maze* generateMaze(int size)
{
	struct maze *maze = malloc(sizeof(struct maze)); 
	maze->cells = calloc(size, size * sizeof(struct cell));
	maze->size = size;
	
	int currentPoint = 0;
	Point *toVisit = malloc(sizeof(Point) * size * size);

	toVisit[currentPoint].x = rand()%size;
	toVisit[currentPoint].y = rand()%size;
	getCell(maze, toVisit[currentPoint])->visited = true;

	while (currentPoint >= 0) {
		Point notVisitedNeighs[4];
		int neighCount = 0;

		struct cell *tmp;
		Point point = {
			.x = toVisit[currentPoint].x,
			.y = toVisit[currentPoint].y
		};

		Point neighs[] = {
			(Point) {.x = 1, .y = 0},
			(Point) {.x = 0, .y = 1},
			(Point) {.x = - 1, .y = + 0},
			(Point) {.x = 0, .y = - 1}
		};

		for (int i = 0; i < 4; ++i) {
			Cell *cell = getCell(maze, addPoints(neighs[i], point));
			if (cell && !(cell->visited)) {
				notVisitedNeighs[neighCount++] = neighs[i];	
			}
		}
		if (neighCount > 0) {
			int chosen = rand() % neighCount;
			
			Point delta = notVisitedNeighs[chosen];
			Point next = addPoints(delta, point);
			Cell *currentCell = getCell(maze, point);
			Cell *nextCell = getCell(maze, next);

			connectCells(currentCell, nextCell, delta);
			nextCell->visited = true;
			currentPoint++;
			toVisit[currentPoint] = next; 
		} else {
			currentPoint--;
		}
	}
	free(toVisit);
	return maze;
}

void printMaze(Maze* maze)
{
	int size = maze->size * 2 + 1;
	PrintMaze *printMaze = malloc(sizeof(Maze)); 
	printMaze->cells = calloc(size, size * sizeof(PrintCell));
	printMaze->size = size;

	for(int i = 0; i < maze->size; i++) {
		for (int j = 0; j < maze->size; j++) {
			PrintCell *cell = getPrintCell(printMaze, (Point) {i*2+1,j*2+1});
			cell->cell = getCell(maze, (Point) {i,j});
			cell->edges = cell->cell->edges;
		}
	}
	
	for(int i = 1; i < size-1; i++) {
		for (int j = 1; j < size-1; j++) {
			if (!(i%2 == 1 && j%2 == 1)) {
				PrintCell *printCell = getPrintCell(
						printMaze, (Point) {i,j});
				if (printCell->cell != NULL)
					break;
				if (getPrintCell(printMaze, (Point) {i+1,j+0})->edges & 0b1000)
					printCell->edges |= 0b0001;
				if (getPrintCell(printMaze, (Point) {i+0,j+1})->edges & 0b0010)
					printCell->edges |= 0b0100;
				if (getPrintCell(printMaze, (Point) {i-1,j+0})->edges & 0b0001)
					printCell->edges |= 0b1000;
				if (getPrintCell(printMaze, (Point) {i+0,j-1})->edges & 0b0100)
					printCell->edges |= 0b0010;
			}
		}
	}

	for(int j = 0; j < size; j++) {
		for (int i = 0; i < size; i++) {
			if (getPrintCell(printMaze, (Point) {i,j})->cell) {
				putchar(' ');
			} else if (getPrintCell(printMaze, (Point) {i,j})->edges != 0) {
				putchar(' ');
			} else if (i == 0 && j == 1) {
				putchar(' ');
			} else if (i == size - 1 && j == size-2) {
				putchar(' ');
			} else {
				printWall(getPrintCell(printMaze, (Point) {i,j})->edges);
			}
		}
		putchar('\n');
	}
}

void main() 
{
	srand(time(NULL));

	int mazeSize;
	printf("Tamaño: ");
	scanf("%d", &mazeSize);

	Maze *maze = generateMaze(mazeSize);
	printMaze(maze);
}
