#!/usr/bin/bash

# Testa recebimento de parametros

if [ $# -eq 0 ]
then
    echo "Falta nome do arquivo a ser tratado"
fi

# Arquivo de saida destino

SAIDA="/tmp/output_2.txt"
> "$SAIDA"

#Acessa o arquivo criado anteriormente formatando saida

while IFS= read -r linha
do
   f=($linha)
   resp=""
   cont=""
   case ${f[0]} in
   '#'|'') printf "%s\n" "${linha}" >> $SAIDA
           ;;
   *) # Imprime primeira parte formatada
      printf -v tmp "%-18s%-11s%s   %s   %s   %s   %-7s   %s   %s" ${f[0]} ${f[1]} ${f[2]} ${f[3]} ${f[4]} ${f[5]} ${f[6]} ${f[7]} ${f[8]}  
      resp+=$tmp
      # Imprime o resto da linha que e variavel
      t=${#f[*]}
      for (( i=9; i<=$(( $t - 1 )); i++ ))
      do
        tmp=$(printf '   %-4s' "${f[$i]}")
        cont+="$tmp"
      done
      # Junta as respostas numa unica linha
      resp+="$cont"
      printf '%s\n' "${resp}" >> $SAIDA
      ;;
esac
done < $1
