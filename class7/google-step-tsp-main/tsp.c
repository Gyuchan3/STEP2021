#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>

// void die(char *s){
//   perror(s);
//   exit(1);
// }

// 町の構造体
typedef struct{
  double x;
  double y;
} City;

typedef struct{
  int *tour;
  double dist;
} Answer;

void swap(int *a, int *b);
double distance(const City a, const City b);
double dist(const City *city, const int *tour, const int i, const int j);
City *read_input(const char *filename, const int n);
void print_tour(const char *filename, const int n, const int tour[n]);
void generate_random_tour(const City *cities, const int n, int tour[n]);
Answer two_opt(const City *cities, const int n);
double solve(const City *cities, const int n, int *tour);

void swap(int *a, int *b){
  int tmp = *a;
  *a = *b;
  *b = tmp;
}

double distance(const City a, const City b){
  return sqrt((a.x - b.x)*(a.x - b.x) + (a.y - b.y)*(a.y - b.y));
}

double dist(const City *city, const int *tour, const int i, const int j){
  return distance(city[tour[i]], city[tour[j]]);
}

City *read_input(const char *filename, const int n){
  City *cities;
  FILE *fp;
  if ((fp=fopen(filename,"r")) == NULL){
    fprintf(stderr, "%s: cannot open file.\n",filename);
    exit(1);
  }

  cities = (City*)malloc(sizeof(City) * n);
  char tmp[50];
  fscanf(fp, "%s", tmp); // 1行目は読み捨てる
  for (int i = 0; i < n; ++i){
    fscanf(fp, "%lf,%lf", &cities[i].x, &cities[i].y);
    // printf("(x, y) = (%lf, %lf)\n", cities[i].x, cities[i].y); // 確認用
  }

  fclose(fp);
  return cities;
}

void print_tour(const char *filename, const int n, const int tour[n]){
  FILE *fp;
  if ((fp=fopen(filename,"w")) == NULL){
    fprintf(stderr, "%s: cannot open file.\n",filename);
    exit(1);
  }

  fprintf(fp, "index\n");
  for (int i = 0; i < n; ++i){
    fprintf(fp, "%d\n", tour[i]);
  }

  fclose(fp);
}

void generate_random_tour(const City *cities, const int n, int tour[n]){
  for (int i = 0; i < n; ++i){
    tour[i] = i;
  }
  // 100回入れかえる
  for (int i = 0; i < 100; ++i){
    int r1 = rand() % (n - 1) + 1;
    int r2 = rand() % (n - 1) + 1;
    // int tmp = tour[r1];
    // tour[r1] = tour[r2];
    // tour[r2] = tmp;
    swap(&tour[r1], &tour[r2]);
  }
}


// Answer generate_greedy_tour(const City *cities, const int n){
//   int tmp_tour[n];
//   int visited[n];
//   memset(visited, 0, sizeof(int) * n); // visitedの中身を0で初期化

//   int current_city = 0;
//   visited[current_city] = 1;
//   tmp_tour[0] =  current_city;
//   for (int i = 0; i < n; ++i){
//     if (visited[i] == 0){

//     }
//   }

// }

Answer two_opt(const City *cities, const int n){
  int tour[n];
  generate_random_tour(cities, n, tour);

  int step = 100;
  for (int s = 0; s < step; ++s){
    int r1 = rand() % (n-1) + 1;
    int r2 = rand() % (n-1) + 1;

    if (r1 > r2) swap(&r1, &r2);
    if ((r2 - r1) <= 2) continue;

    int next_r1 = (r1 + 1) % n;
    int prev_r2 = (r2 - 1 + n) % n;
    if ((dist(cities, tour, r1, next_r1) + dist(cities, tour, r2, prev_r2)) > 
        (dist(cities, tour, r1, prev_r2) + dist(cities, tour, r2, next_r1))){
          while(1){
            r1 = (r1 + 1) % n;
            r2 = (r2 - 1 + n) % n;
            swap(&tour[r1], &tour[r2]);
            if (0 <= r2 - r1 && r2 - r1 <= 1) break;
          }
      }
  }

  double sum_dist = 0;
  for (int i = 0; i < n; ++i){
    // const int cur = tour[i];
    // const int next = tour[(i + 1) % n];
    // sum_dist += distance(cities[cur], cities[next]);
    sum_dist += dist(cities, tour, i, (i + 1) % n);
  }

  int *result_tour = (int*)calloc(n, sizeof(int));
  memcpy(result_tour, tour, sizeof(int) * n);
  return (Answer){.dist = sum_dist, .tour = result_tour};    
}

double solve(const City *cities, const int n, int *tour){
  // Answer answer = generate_random_tour(cities, n);
  // Answer answer = generate_greedy_tour(cities, n);
  Answer answer = (Answer){.dist = 1e20}; // 適当に大きい初期値
  for (int i = 0; i < 10; ++i){
    Answer result = two_opt(cities, n);
    if (result.dist < answer.dist){
      free(answer.tour);
      answer = result;
    }
  }
  memcpy(tour, answer.tour, sizeof(int) * n);

  return answer.dist;
}

int main(int argc, char **argv){
  if (argc != 2){
    fprintf(stderr, "usage: %s <input file's number>\n", argv[0]);
    exit(1);
  }
  srand((unsigned)time(NULL));

  char input_filename[20];
  sprintf(input_filename, "input_%s.csv", argv[1]);

  int N[] = {5, 8, 16, 64, 128, 512, 2048, 8192};
  int n = N[atoi(argv[1])]; // 都市数
  City *cities = read_input(input_filename, n);

  int *tour = (int*)calloc(n, sizeof(int));
  double dist = solve(cities, n, tour);
  printf("path_length: %lf\n", dist);

  char output_filename[20];
  sprintf(output_filename, "output_%s.csv", argv[1]);
  print_tour(output_filename, n, tour);

  free(tour);
  free(cities);

  return 0;
}