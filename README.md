# ACM_tasks

## TASK_1: Automate the vit wifi login +  automate the login procedure itself
## How I managed to do it:
- As soon as I saw the task the forst thing that popped in my mind is the `selenium tool` and as am good at python I created a pyhton script using selenium package with some help from chatgpt.
- then i used batch to automate it at the start up (I have some knowledgeon basic batch scripting)

## How to use this:
- Downlaod the `python` and `batch` file.
- save them in the `shell:script`, which you'll find by running shell:script in `run`
- click on the python file and edit it in any text file and replace the `your_username` and `your_password` with respectibve credentials

 ```@python
# Replace with your own login credentials
username = "your_username"
password = "your_password"
```
### Remember to enable the automatic connect in wifi ;)

## Task_2: Given is a binary file run the file and solve the q if answer is correct display the flag and get the answer while also specifying the input value

### The flag is in the `flag.txt`

## How I found the flag.
- As it's a binary file I used `rabin2` tool to extract the binary file info
```
rabin2 -I q
```
- Then I found that the language used was `C`
- Then I used `strings` command to search through the binary data to find and display sequences of printable characters.
- I came across `acm_ftw` just before `flag.txt`. I guessed it as flag to confirm this I used a tool `ghidra`, used to analyze and debugging the binary file.
  There in the `switch case` i came across a `check_win()` fucntion under case 4 and when I inspected . This appeared
```@C
void check_win(void)

{
  int iVar1;
  FILE *__stream;
  long in_FS_OFFSET;
  char local_58 [72];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  iVar1 = strcmp(safe_var,"ACMR");
  if (iVar1 == 0) {
    puts("\nacm_ftw ");
    __stream = fopen("flag.txt","r");
    fgets(local_58,0x40,__stream);
    puts(local_58);

```
-By this I confirmed the flag.
