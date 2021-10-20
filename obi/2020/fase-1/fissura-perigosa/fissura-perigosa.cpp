#include <cstdio>

int map[502][502];
int size, intensity;

// vetores de auxílio, que servirão como 
// arestas no grafo e ajudam a "navegar" 
// pelo mapa.
int dx[5] = {1, 0, -1, 0};
int dy[5] = {0, 1, 0, -1};

// depth-first search
void dfs(int i, int j){
	
	map[i][j] = 10;
	for (int k = 0; k < 4; k++) {
		int ii = i + dx[k];
		int jj = j + dy[k];
		if(ii <= 0 || ii > size || jj <= 0 || j > size) continue;
		if(map[ii][jj] > intensity) continue;
		dfs(ii, jj);
	}
}

int main() {
    scanf("%d %d", &size, &intensity);

    for (int i = 1; i < size + 1; i++) {
        for (int j = 1; j < size + 1; j++) {
            char c;
            scanf(" %c", &c);
            map[i][j] = c - '0'; 
        }
    }
    
    // Run algorithm
    if ((map[1][1]) <= intensity) {
        dfs(1, 1);
    }

    // Print map
    for (int i = 1; i < size + 1; i++) {
        for (int j = 1; j < size + 1; j++) {
            if (map[i][j] > 9) printf("*");
            else printf("%d", map[i][j]);
        }
        printf("\n");
    }
}