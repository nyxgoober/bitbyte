$nomention
$botTyping
$if[$getVar[isAdmin;$authorID]!=yes]
$eval[$getVar[unauthorisedUI]]
$stop
$endif

$if[$mentioned[1]==]
$addContainer[noUsr]
$addTextDisplay[## <:xmark:1511346908701134848> No Victim;noUsr]
$addTextDisplay[Please specify a user to allow to talk!;noUsr]
$stop
$endif

$untimeout[]
$addContainer[done]
$addTextDisplay[## <:check:1511347308929744938> Unmute;done]
$addTextDisplay[<@$mentioned[1]> is now allowed to talk again.;done]