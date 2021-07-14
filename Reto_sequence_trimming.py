class trim:

    def __init__(self, fastq) -> None:
        self.fastq = open (fastq).readlines ()
        
    def window (self, window_size, quality) -> None:
        sec_len = 0
        last_sec_len = float ("-inf")

        # parse the document and take quality 
        for i in range (0, len (self.fastq), 4):
            posible_cuts = list ()

            id = self.fastq [i]
            sep = self.fastq [i+2]
            sec_quality = self.fastq [i+3].strip ()
            window_phre_score = list (map (lambda letter: ord (letter)-33 , sec_quality [:window_size]))
            #print (window_phre_score)
            print (sec_quality)
            if sum (window_phre_score) /window_size < quality:
                posible_cuts.append ((0, window_size-1))

            # we advance in the sec_quiality
            for ascii in range (4, len (sec_quality)):
                del window_phre_score [0]
                window_phre_score.append (ord (sec_quality [ascii])-33)
                #print (window_phre_score)

                if sum (window_phre_score) /window_size > 20:
                    #posible_cuts.append ((ascii-(window_size-1), ascii))
                    sec_len += 1
                else:
                    if last_sec_len < sec_len:
                        last_sec_len = sec_len
                        left_right_cut = () 
                    sec_len = 0

            print (id)
            print (last_sec_len)
            sec_len = 0
            break
            






trim ("test_sanger.fastq").window (4, 20)
        