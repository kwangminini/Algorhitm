#include <iostream>
#include <cstdio>
#include <string.h>

#define MAX_SIZE 10000
typedef struct _stack {
	int arr[MAX_SIZE];
	int top;
}Stack;


void StackInit(Stack * sp) {
	sp->top = -1;
}
void StackPop(Stack * sp) {
	if (sp->top != -1) {
		printf("%d\n", sp->arr[sp->top]);
		sp->top = sp->top - 1;
	}
	else
		printf("-1\n");
}
void StackSize(Stack * sp) {
	printf("%d\n", sp->top + 1);
}
void StackEmpty(Stack * sp) {
	if (sp->top == -1)
		printf("1\n");
	else
		printf("0\n");
}
void StackTop(Stack * sp) {
	if (sp->top == -1)
		printf("-1\n");
	else
		printf("%d\n", sp->arr[sp->top]);
}
void StackPush(Stack * sp, int num) {
	sp->arr[sp->top + 1] = num;
	sp->top += 1;
}

int main() {
	Stack st;
	StackInit(&st);
	int n,num;
	char str[10];
	scanf("%d", &n);
	while (n--) {
		scanf("%s", str);
		if (!strcmp(str, "push")) {
			scanf("%d", &num);
			StackPush(&st, num);
		}
		if (!strcmp(str, "pop")) {
			StackPop(&st);
		}
		if (!strcmp(str, "empty")) {
			StackEmpty(&st);
		}
		if (!strcmp(str, "size")) {
			StackSize(&st);
		}
		if (!strcmp(str, "top")) {
			StackTop(&st);
		}
	}
	
	return 0;
}