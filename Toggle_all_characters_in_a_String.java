// Java program to toggle all characters in a string
// convert lower case to upper case and vice versa


class GFG 
{

static void toggleChars(char str[])
{
    for (int i=0; i<str.length; i++)
    {
        if (str[i]>='A' && str[i]<='Z')
            str[i] = (char) (str[i] + 'a' - 'A');
        else if (str[i]>='a' && str[i]<='z')
            str[i] = (char) (str[i] + 'A' - 'a');
    }
}

// Driver code 
public static void main(String[] args) 
{
    char str[] = "GeKf@rGeek$".toCharArray();
    toggleChars(str);
    System.out.println("String after toggle ");
    System.out.println(String.valueOf(str));
}
}
