#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<time.h>
#include<string.h>
#include <sys/types.h> 
#include <sys/stat.h>
#include <fcntl.h>

double master_key;
char name[100];
int guest_key=1;
int suppppper_key=2;
int (*hello)();

unsigned int init() {
	unsigned char buffer;
	int f = open("dev/urandom", O_RDONLY);
	read(f, &buffer, 1);
	srand(buffer);
	system("/usr/bin/clear");
	setvbuf(stdout, 0, 2, 0);
	setvbuf(stdin, 0, 2, 0);
	setvbuf(stderr, 0, 2, 0);
	memset(name, 0, 0x64);
	srand((unsigned int)time(0));
	master_key = rand();
	return alarm(0x1fu);
}

int get_point() {
	char name1[100] = {};
	int num = 0;
	printf("����� �̸��� �����Դϱ�?(input name only english)\n");
	read(0, &name1, 0x64);
	strcpy(name, name1);
	printf("%s��, ��� �̸��� ������!!!\n", name);
	for (int i = 0; i < (strlen(name)); i++)
	{
		//name[i%strlen(name)] ^= i;
		num += (int)(name[i]);
	}
	if (num == 0)
	{
		printf("����!����!����!");
		exit(1);
	}
	printf("%d���Դϴ�!!\n", num % 100);
	if (num % 100 == 50) {
		printf("���̶� ���� ���!! �Ǹ��ϱ���?!?!\n");
		return num%100;
	}
	else if (0 < (num % 100)) {
		if ((num % 100) < 50)
			printf("�Ǹ��Ұ� ����� ���� ���� �� �Ǹ��� ���ΰɿ�?!?\n");
		else
			printf("�̺��� �� �Ǹ��� �̸��� ���� ���߾��...\n");
		return num%100;
	}
	else {
		printf("100���̶���? ������ġ�� ���ƿ�... ����� ��¥ �̸��� �˷��ּ���!!!\n");
		return num%100;
	}
}
void comment() {
	printf("1. get_point\n");
	printf("2. lucky_chance!\n");
	printf("3. ������ ����~!\n");
	printf("4. ���Ѿ��!\n");
}
int call();
int have_auth(int point) {
	char a;
	scanf("%c", &a);
	if (a == 'y' || a == 'Y')
	{	
		if (point >= 999999999)
		{
			return master_key;
		}
		else if (point >= 10)
		{
			return suppppper_key;
		}
		else if (point >= 1)
			return guest_key;
		hello = &call;
		
	}
	(*hello)();
}
int lucky_chance() {
	printf("choose one number\n");
	int lucky = 0;
	scanf("%d", &lucky);
	if (lucky == rand())
	{
		printf("Congratuation!!\n");
		return 999999999;
	}
	__asm(
			"NOP;"
			"NOP;"
			"NOP;"
			"NOP;"
			"NOP;"
			"NOP;"
			"NOP;"
			"NOP;"
	     );
	
}
void win() {
        printf("Can you get a key?");
        system("/bin/sh");
}

int call() {
        if (name[0] == '\x00')
        {
                printf("�ʴ���� ���� �մ��Դϴ�.\n");
                exit(1);
        }
        printf("%s��, �湮�� ȯ���մϴ�.\n", name);
}

void open_door(int a) {
	if (a == master_key)
		win();
}
int main() {
	init();
	
	int i = 0;
	int num = 0;
	int auth;
	double point; //card == key����

	while(1){
		comment();
		scanf("%d", &num);
		
		if (num == 1)
		{
			point = get_point(); // ���⼭ point ����
		}
		else if (num == 2)
		{
			point = lucky_chance();
		}
		else if (num == 3)
		{
			open_door(point);
		}
		else if (num == 4) {
			have_auth(auth);
		}
		else
			exit(1);
		
	}

	return 0;
}
