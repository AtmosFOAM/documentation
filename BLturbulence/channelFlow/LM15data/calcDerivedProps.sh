# Calculate nut from Production/(dU/dy)^2
# and compare with Cmu k^2/epsilon

u_tau=`grep u_tau LM_Channel_5200_mean_prof.dat | head -1 | awk '{print $6}'`
nu=`grep Kinematic LM_Channel_5200_mean_prof.dat | head -1 | awk '{print $6}'`
delta=`grep delta LM_Channel_5200_mean_prof.dat | head -1 | awk '{print $7}'`
Cmu=0.09
#kappa=0.384
kappa=0.415

echo '#' u_tau = $u_tau > nut.dat
echo '#' nu = $nu >> nut.dat
echo '#y/delta   y^+   nut^+ (P/dUdz^2)   nut   nutRANS (Cmu k^2/epsilon) nutkl (l root(k)) nutkl^+ l^2dU/dy length (nut/Cmu k^.5)' >> nut.dat

paste <(tail -n +73 LM_Channel_5200_mean_prof.dat) \
      <(tail -n +75 LM_Channel_5200_RSTE_k_prof.dat) \
      <(tail -n +76 LM_Channel_5200_vel_fluc_prof.dat) \
      | awk '{print $1, $2, $9/$4^2, $9/$4^2*'$nu', '$nu'*'$Cmu'*($24)^2/$14, 
              '$kappa'*$1*'$delta'*sqrt($24)*'$u_tau', '$kappa'*$2*sqrt($24), 
              ('$kappa'*$2)^2*$4 $9/$4^2, $9/$4^2*'$nu'/'$Cmu'^.25/($24+1e-16)^0.5/'$u_tau'}' \
        >> nut.dat

gmtPlot plotnut.gmt
ev nut.eps
