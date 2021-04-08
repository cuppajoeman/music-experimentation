%%%%
\version "2.22.0"

%% -----
%% Option 1:
%% Use a procedure to convert a number to pitch:
#(define (: r i)
   (apply
    ly:make-pitch
    (cons (1- (floor (/ (+ r i) 12)))
          (list-ref `((0 0) (0 ,SHARP) (1 0) (1 ,SHARP)
                      (2 0) (3 0) (3 ,SHARP) (4 0)
                      (4 ,SHARP) (5 0) (5 ,SHARP) (6 0))
                    (modulo (+ r i) 12)))))


{
  {
    $(: 0 0)''8 $(: 0 2)'' $(: 0 4)'' $(: 0 7)'' $(: 0 11)'' $(: 0 7)'' $(: 0 9)'' $(: 0 11)'' 
    $(: 0 7)'' $(: 0 4)'' r4  $(: 0 0)'''8 $(: 0 11)'' $(: 0 9)'' $(: 0 7)''
    $(: 2 4)''4  $(: 2 2)''8  $(: 2 4)''~  $(: 2 4)''2
    r8  $(: 2 4)'' $(: 2 5)'' $(: 2 7)'' $(: 2 4)'' $(: 2 0)'' r  $(: 2 2)''   
  }
  {
    $(: 2 3)''4  $(: 2 0)''8  $(: 2 2)'' $(: 2 3)''4  $(: 2 0)''8 $(: 2 2)'' 
    $(: 7 10)'8  $(: 7 4)'4  $(: 7 7)'8 r $(: 7 4)' $(: 7 7)' $(: 7 10)' 
    $(: 0 4)'' $(: 0 0)'' $(: 0 4)'' $(: 0 7)'' $(: 0 11)'' $(: 0 9)'' $(: 0 7)'' $(: 0 4)''
    $(: 7 10)' $(: 7 7)' r4 r2
  }
}
