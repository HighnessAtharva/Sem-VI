# factorial function 

factorial()
{
    num=$1
    if [ $num -eq 1 ]; then
        echo 1
    else
        temp=$((num-1))
        result=$(factorial $temp)
        echo $((result * $1))
    fi
}

echo "Enter a number: "
read num
factorial $num