import Foundation
import ArgumentParser

struct RocketFuel: ParsableCommand {
  @Option(name: .shortAndLong, help: ArgumentHelp("Path to input file that contains a list of masses."))
  var inputMassList: String = "."

  @Flag(name: .shortAndLong)
  var verbose: Bool = false

  mutating func run() throws {
    // sum list of determine fuel for each payload mass

    guard let fileURL = URL(string: inputMassList),
      let handle = try? FileHandle(forReadingFrom: fileURL),
      let delimiterData = "\n".data(using: .utf8) else {
      print("Failed to find file")
      return
    }

    let reader = LineReader(handle: handle, lineDelimiterData: delimiterData)
    var fuelSum = 0

    for line in reader {
      var totalFuelForAdditionalWeight = 0
      if let mass = Int(line) {
        var fuelForMass = fuelRequirement(forMass: mass)
        if verbose {
          print("Initial Fuel: \(fuelForMass)")
        }
        totalFuelForAdditionalWeight += fuelForMass

        // determine additional fuel for weight of addtional fuel
        var additionalFuel = 1
        while additionalFuel > 0 {
          additionalFuel = fuelRequirement(forMass: fuelForMass)
          if additionalFuel > 0 {
            if verbose {
              print("Additional Fuel: \(additionalFuel)")
            }
            totalFuelForAdditionalWeight += additionalFuel
            fuelForMass = additionalFuel
          }
        }
        fuelSum += totalFuelForAdditionalWeight
      }
    }

    print("Total fuel requirements: \(fuelSum)")
  }

  func fuelRequirement(forMass mass: Int) -> Int {
	  return Int(floor(Double(mass)/Double(3))) - 2
  }
}

RocketFuel.main()
