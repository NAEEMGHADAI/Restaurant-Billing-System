#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
#include<malloc.h>

struct node 
{
	char name[100];
	int roll;
	float marks;
	float per;
	float poin;
	float attan;
	struct node *next;
};

struct node *studentDetails(struct node*);
struct node *deleteAttandance(struct node*);
struct node *showDetails(struct node*);
struct node *showAttandance(struct node*);
struct node *showPointer(struct node *);
struct node *start = NULL;

int main()
{
	int choice,pass;
	do
	{
		printf("\n*****MAIN MENU*****\n");
		printf("FOR TEACHERS\n");
		printf("ENTER YOUR CHOICE\n");
		printf("1-TO ADD MARKS AND ATTANDANCE\n2-DELETE ROLL NO.\n");
		printf("FOR STUDENTS\n");
		printf("3-TO SEE ATTANDANCE AND POINTER\n4-TO SEE ATTANDANCE\n5-TO SEE POINTER\n6-EXIT\n");
		
		scanf("%d",&choice);
		
		switch(choice)
		{
			
			case 1:
				printf("ENTER YOUR PASSWORD\n");
				scanf("%d",&pass);
			
				if(7787==pass)
				{
					start=studentDetails(start);
				}
				else
				{
					system("cls");
					printf("INVALID PASSWORD\n");
				}
				break;
			
			case 2:
				printf("ENTER YOUR PASSWORD\n");
				scanf("%d",&pass);
			
				if(7787==pass)
				{
					start=deleteAttandance(start);;
				}
				else
				{
					system("cls");
					printf("INVALID PASSWORD\n");
				}
				break;
			
			case 3:
				start=showDetails(start);
				break;	
		    
			case 4:
		    	start=showAttandance(start);
		    	break;
			
			case 5:
				start=showPointer(start);
		    	break;
		
		}
	
	}while(choice!=6);
	
	return 0;
}



struct node *studentDetails(struct node *start)
{
	struct node *ptr,*new_node;
	
	int num,i=0;
	float per,poin,attan,marks,total;
	char c[100];
	
	printf("ENTER NAME OF THE STUDENT: \t");
	scanf("%s",c);
	
	printf("\nENTER ROLL NO: \t");
	scanf("%d",&num);
	
	printf("\nENTER FINAL EXAM OUT OF MARKS: \t");
	scanf("%f",&total);
	
	printf("\nENTER FINAL EXAM MARKS: \t");
	scanf("%f",&marks);
	
	printf("\nENTER STUDENTS ATTANDANCE: \t");
	scanf("%f",&attan);
	
	
	new_node=(struct node*)malloc(sizeof(struct node));
	
	for(i=0;i<strlen(c);i++)
	{
		new_node->name[i]=c[i];
	}
	
	new_node->roll=num;
	new_node->marks=marks;
	
	per=(marks/total)*100;
	poin=per/9;
    
	new_node->per=per;
    new_node->poin=poin;
    new_node->attan=attan;
    
	printf("PERCENTAGE: %f\n",per);
    printf("POINTER: %f\n",poin);
	
	ptr=start;
	
	if(start==NULL)
	{
		start=new_node;
		start->next=NULL;
	}
	else
	{
		while(ptr->next!=NULL)
		{
			ptr=ptr->next;
		}
		ptr->next=new_node;
		new_node->next=NULL;
	}
	
	return start;
}

struct node *showAttandance(struct node *start)
{
	struct node *ptr1,*ptr2;
	float temp;
	int temp1;
	char temp2[50];
	
	ptr1=start;
	if(start==NULL)
	{
		printf("NO STUDENT DETAILS UPLOADED TILL NOW\n");
	}
	else
	{
		while(ptr1->next!=NULL)
	    {
		    ptr2=ptr1->next;
		    while(ptr2!=NULL)
		    {
			    if(ptr1->attan<ptr2->attan)
			    {
				    temp=ptr1->attan;
					ptr1->attan=ptr2->attan;
					ptr2->attan=temp;
				
					temp1=ptr1->roll;
					ptr1->roll=ptr2->roll;
					ptr2->roll=temp1;
				
					strcpy(temp2,ptr2->name);
					strcpy(ptr2->name,ptr1->name);
					strcpy(ptr1->name,temp2);
				}
				ptr2=ptr2->next;
			}
			ptr1=ptr1->next;
	    }
    
	
	
		ptr1=start;
	
		printf("ROLL\tNAME\tATTANDANCE\n");
		while(ptr1->next!=NULL)
		{
			printf("%d\t",ptr1->roll);
			printf("%s\t",ptr1->name);
			printf("%f\n",ptr1->attan);
			ptr1=ptr1->next;
		}
	
		printf("%d\t",ptr1->roll);
		printf("%s\t",ptr1->name);
		printf("%f\n",ptr1->attan);
	}
	return start;
}



struct node *showPointer(struct node *start)
{
	struct node *ptr1,*ptr2;
	float temp;
	int temp1;
	char temp2[50];
	
	ptr1=start;
	
	if(start==NULL)
	{
		printf("NO STUDENT DETAILS UPLOADED TILL NOW\n");
	}
	else
	{
		while(ptr1->next!=NULL)
		{
			ptr2=ptr1->next;
			while(ptr2!=NULL)
			{
				if(ptr1->poin<ptr2->poin)
				{
					temp=ptr1->poin;
					ptr1->poin=ptr2->poin;
					ptr2->poin=temp;
				
					temp1=ptr1->roll;
					ptr1->roll=ptr2->roll;
					ptr2->roll=temp1;
				
					strcpy(temp2,ptr2->name);
					strcpy(ptr2->name,ptr1->name);
					strcpy(ptr1->name,temp2);
				
				}
				ptr2=ptr2->next;
			}
			ptr1=ptr1->next;
		}
	
		ptr1=start;
	
		printf("ROLL\tNAME\tPOINTER\n");
		while(ptr1->next!=NULL)
		{
			printf("%d\t",ptr1->roll);
			printf("%s\t",ptr1->name);
			printf("%f\n",ptr1->poin);
			ptr1=ptr1->next;
		}
	
		printf("%d\t",ptr1->roll);
		printf("%s\t",ptr1->name);
		printf("%f\n",ptr1->poin);
	}
	return start;
}

struct node *showDetails(struct node *start)
{
	struct node *ptr;
	int roll;
	ptr=start;
	if(start==NULL)
	{
		printf("NO STUDENT DETAILS UPLOADED TILL NOW\n");
	}
	
	else
	{
		printf("ENTER YOUR ROLL NO.\n");
		scanf("%d",&roll);
	
		while(ptr->roll!=roll)
		{
			ptr=ptr->next;
		}
	
		printf("ROLL\tNAME\tATTAND\tPOINTER\n");
		printf("%d\t",ptr->roll);
		printf("%s\t",ptr->name);
		printf("%f\t",ptr->attan);
		printf("%f\n",ptr->poin);
	
		if(ptr->poin<4)
		{
			printf("NOT ELIGIBLE TO SEAT IN FUTHER EXAMS\n******KT*******\n");
		}
	}
	return start;
}

struct node *deleteAttandance(struct node *start)
{
	struct node *ptr,*preptr;
	
	int val;
	ptr=start;
	
	printf("ENTER THE ROLL NO. TO BE DELETED:\n");
	scanf("%d",&val);
	if(start==NULL)
	{
		printf("NO STUDENT DETAILS UPLOADED TILL NOW\n");
		return start;
	}
	
	else if(ptr->roll==val)
	{
		
		ptr=ptr->next;
		free(ptr);
		
		return start;
	}
	else
	{
		
		while(ptr->roll!=val)
		{
			preptr=ptr;
			ptr=ptr->next;
		}
		
		preptr->next=ptr->next;
		free(ptr);
		
		return start;
	}
}
