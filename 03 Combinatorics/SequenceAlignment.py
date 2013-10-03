import pylab

# Gene sequences got from database

chimpanzee = "mtlgrrlaclflacvlpalllggtalaseivggrrarphawpf"\
    "mvslqlrgghfcgatliapnfvmsaahcvanvvravrvgahlsrreptrqvf"\
    "avqrikglngsatinanvqvaqlpaqgrhlgngvqclamgwgllgrnrgias"\
    "vlqelnvtvvtslcrrsnvctlvrgrragvcfgdsgsplvcnglihgiasfv"\
    "rggcasglypdafapvaqfvnwinsiiqrsednpcphprdpdpasrth"
cat = "mtpsrrsagpalapvllamllggpalaseivggrparphawpfmvslqlr"\
    "gghfcggtliapnfvmsaahcvdglnfrsvvavlgahdlrrreptrqmftiq"\
    "rvfengfdpqrllndivilqlngsatinsnvrvarlpaqnqgvgsgvqclam"\
    "gwgqlgttqpppnilqelnvtvvttlcprsnvctlvprrqagicfgdsggpl"\
    "vcngliqgidsfirgscgsgfypdafapvaqfanwidsiirrqddrpsvhpr"\
    "dpasrtl"
human = "mtlgrrlaclflacvlpalllggtalaseivggrrarphawpfmvslq"\
    "lrgghfcgatliapnfvmsaahcvanvnvravrvvlgahnlsrreptrqvfa"\
    "vqrifengydpvnllndivilqlngsatinanvqvaqlpaqgrrlgngvqcl"\
    "amgwgllgrnrgiasvlqelnvtvvtslcrrsnvctlvrgrqagvcfgdsgs"\
    "plvcnglihgiasfvrggcasglypdafapvaqfvnwidsiiqrsednpcph"\
    "prdpdpasrth"
dog = "mtarrvpagpalgpllllatllpgpalaseivggrpaqphawpfmvslqr"\
    "rgghfcggtliapnfvmsaahcvdglnfrsvvvvlgahdlgerestrqlfav"\
    "qrvfengfdpvrlvndivllqlngsatinanvqvarlpaqnqgvgngvqcla"\
    "mgwgqlgtaqppprilqelnvtvvttlcrrsnvctlvprrragicfgdsggp"\
    "lvcngliqgidsfirgscasgffpdafapvaqfvdwinsiirrppalpparp"\
    "gqqdpergaarapppaphrprptq"

species = [human, chimpanzee, dog, cat]

alignment = [];

for n in range(len(species)):
    for m in range(n+1,len(species)):
        
        alignment += [0]
        
        pylab.figure()

        for i in range(len(species[n])-5):
            for j in range(len(species[m])-5):
                match = True
                for k in range(5):
                    if species[n][i+k] != species[m][j+k]:
                        match = False
                
                if match:
                    pylab.plot(i, j, 'bo')
                    alignment[-1] += 1

            
print "Human - Chimpanzee alignment : ", alignment[0]
print "Human - Dog alignment : ", alignment[1]
print "Human - Cat alignment : ",alignment[2]
print "Chimpanzee - Dog alignment : ",alignment[3]
print "Chimpanzee - Cat alignment: ", alignment[4]
print "Dog - Cat alignment : ", alignment[5]